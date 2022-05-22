# -*- coding: utf-8 -*-
import sqlalchemy.engine
import cx_Oracle
import re
import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from configs.db import DB, DB_DECANAT
from utils.sendemail import NSTUSender
import pandas as pd

SQLALCHEMY_DATABASE_URL = f"{DB['name']}+{DB['driver']}://{DB['username']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['section']}"
DECANATUSER_URL = f"{DB['name']}+{DB['driver']}://{DB_DECANAT['username']}:{DB_DECANAT['password']}@{DB['host']}:{DB['port']}/{DB['section']}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
engine_decanat = create_engine(DECANATUSER_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_raw_connection():
    """для вызовы хранимых процедур"""
    return create_engine(SQLALCHEMY_DATABASE_URL, echo=False).raw_connection()


def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]

    new_list = []
    for row in cursor:
        row_dict = dict()
        for col in columns:
            if isinstance(row[columns.index(col)], datetime):
                row_dict[col] = row[columns.index(col)].isoformat()
            else:
                row_dict[col] = row[columns.index(col)]
        new_list.append(row_dict)
    return new_list


def get_from_function(_engine: sqlalchemy.engine.Engine, func_name: str, *args) -> list:
    with _engine.begin() as conn:
        cursor = conn.connection.cursor()
        res = cursor.callfunc(name=func_name, returnType=cx_Oracle.CURSOR, parameters=args)
        results = rows_to_dict_list(res)
        cursor.close()
        return results


def get_from_grid(func_name: str, columns: list, filter_str: str, params_list: list) -> pd.DataFrame:
    list_res = get_from_function(engine_decanat, func_name, *params_list)
    cols = []
    cols_dict = {}
    for i in columns:
        cols_dict[i['FIELD']] = i['CAPTION']
        cols.append(i['CAPTION'])
    new_list_res = []
    for i in list_res:
        j = {}
        for k in i:
            try:
                j[cols_dict[k]] = i[k]
            except KeyError:
                pass
        new_list_res.append(j)
    # преобразуем в датафрейм
    df = pd.DataFrame(new_list_res)
    fltrs = [[j.strip().upper() for j in re.split('(=|<>|>|<)', i)] for i in [i.strip() for i in filter_str.split('and')]]
    # преобразуем строку фильтрации
    for i in fltrs:
        i[0] = f"`{cols_dict[i[0]]}`"
        # для строковой фильтрации
        if '*' in i[2] and i[1] == '=':
            i[1] = ".str.contains"
            i[2] = f"('^{i[2].replace('*', '.*')}$')"
    # собираем обратно
    filter_str = " and ".join([''.join(i) for i in fltrs])
    return df.query(filter_str)


def send_xlsx(stored_proc: str, filter_str: str, params: str, columns: str, userid: int, sid: int):
    """
    выгрузка хранимой процедуры в excel и отправка на почту
    :param stored_proc: хранимая процедура
    :param filter_str: строка фильтрации
    :param params: параметры
    :param columns: столбцы
    :param userid: ид пользователя (decanatuser)
    :param sid: ид сессии
    :return:
    """
    params = params.strip().split(',')
    if params == ['']:
        params = []
    res = get_from_grid(stored_proc,
                        json.loads(columns),
                        filter_str,
                        params)
    with engine_decanat.begin() as conn:
        cursor = conn.connection.cursor()
        email = cursor.callfunc(name="decanatuser.for_ad_pkg.get_decanatuser_mail",
                                returnType=cx_Oracle.DB_TYPE_NVARCHAR,
                                parameters=[userid, ])
    res.to_excel("output.xlsx", index=False)
    sender = NSTUSender.get_default_sender()
    sender.send("", "", 'noreply@corp.nstu.ru', email, ['output.xlsx'])


if __name__ == "__main__":
    send_xlsx('decanatuser.OTDEL2.get_facultet_list',
              "SHORTNAME = *Д* and PK>6",
              "",
              '[{"FIELD": "SHORTNAME", "CAPTION": "Факультет"}, {"FIELD": "PK", "CAPTION": "Ид"}]',
              2, 1)
