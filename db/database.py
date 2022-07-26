# -*- coding: utf-8 -*-
import sqlalchemy.engine
import cx_Oracle
import re
import json
from sqlalchemy import create_engine, Table, Column, Integer, Date, String, Numeric, text, insert, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from configs.db import DB, DB_DECANAT, DB_SANDBOX, DB_TEZIS
from utils.sendemail import NSTUSender
import pandas as pd
import logging

SQLALCHEMY_DATABASE_URL = f"{DB['name']}+{DB['driver']}://{DB['username']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['section']}"
DECANATUSER_URL = f"{DB['name']}+{DB['driver']}://{DB_DECANAT['username']}:{DB_DECANAT['password']}@{DB['host']}:{DB['port']}/{DB['section']}"
SANDBOX_URL = f"{DB_SANDBOX['name']}://{DB_SANDBOX['username']}:{DB_SANDBOX['password']}@{DB_SANDBOX['host']}:{DB_SANDBOX['port']}/{DB_SANDBOX['section']}"
TEZIS_URL = f"{DB_TEZIS['name']}://{DB_TEZIS['username']}:{DB_TEZIS['password']}@{DB_TEZIS['host']}:{DB_TEZIS['port']}/{DB_TEZIS['section']}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
engine_decanat = create_engine(DECANATUSER_URL, echo=False)
engine_sandbox = create_engine(SANDBOX_URL, echo=False)
engine_tezis = create_engine(TEZIS_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_decanat)
SessionSandbox = sessionmaker(autocommit=False, autoflush=False, bind=engine_sandbox)
SessionTezis = sessionmaker(autocommit=False, autoflush=False, bind=engine_tezis)
Base = declarative_base()
metadata = Base.metadata

t_priority_on_date = Table(
    'priority_on_date', metadata,
    Column('years', Integer),
    Column('on_date', Date),
    Column('name', String(2000)),
    Column('vals', Numeric),
    Column('fk_indicator', Integer),
    Column('descr', String(100)),
    schema='metabase'
)

src_t_priority_on_date = Table(
    'vw$priority_indicator_on_date', metadata,
    Column('years', Integer),
    Column('on_date', Date),
    Column('name', String(2000)),
    Column('vals', Numeric),
    Column('fk_indicator', Integer),
    Column('descr', String(100)),
    schema='metauser'
)

t_priority_results = Table(
    'priority_results', metadata,
    Column('years', Integer),
    Column('fk_indicator', Integer),
    Column('name', String(1000)),
    Column('vals', Numeric),
    Column('descr', String(1000)),
    schema='metabase'
)


src_t_priority_results = Table(
    'vw$priority_indicator_result', metadata,
    Column('years', Integer),
    Column('fk_indicator', Integer),
    Column('name', String(1000)),
    Column('vals', Numeric),
    Column('descr', String(1000)),
    schema='metauser'
)

t_priority_nich = Table(
    'priority_nich', metadata,
    Column('years', Integer),
    Column('sp', String(100)),
    Column('projectname', String(500)),
    Column('subproject', String(500)),
    Column('priority_plan', Numeric),
    Column('plan_prihod', Numeric),
    Column('paid', Numeric),
    Column('ostatok_plan', Numeric),
    Column('ostatok_fakt', Numeric),
    Column('indikator', String(500)),
    schema='metabase'
)


src_t_priority_nich = Table(
    'vw$priority_nich', metadata,
    Column('years', Integer),
    Column('sp', String(1000)),
    Column('projectname', String(1000)),
    Column('subproject', String(1000)),
    Column('priority_plan', Numeric),
    Column('plan_prihod',Numeric),
    Column('paid', Numeric),
    Column('ostatok_plan', Numeric),
    Column('ostatok_fakt', Numeric),
    Column('indikator', String(500)),
    schema='metauser'
)



TABS = {'priority_on_date': (t_priority_on_date, src_t_priority_on_date),
        'priority_results': (t_priority_results, src_t_priority_results),
        'priority_nich': (t_priority_nich, src_t_priority_nich)
        }


class OracleView(Base):
    __tablename__ = 'oracle_views'
    __table_args__ = {'schema': 'metabase'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('metabase.oracle_views_id_seq'::regclass)"))
    user_name = Column(String(100))
    view_name = Column(String(100))
    to_load = Column(Integer, nullable=False, server_default=text("1"))
    table_name = Column(String(100), nullable=False)


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


def load_assets(file_path: str):
    """
    :param file_path: путь к файлу
    :return:
    """
    logging.info('starting')
    cols_src = ['Инвентарный номер', 'Дата принятия к учету', 'Срок полезного использования', 'МОЛ',
                'ЦМО.Место хранения', 'Дата ввода в эксплуатацию', 'Счет', 'Основное средство', 'Основное средство.Код',
                'Балансовая стоимость', 'Количество', 'Сумма амортизации', 'Остаточная стоимость']

    cols_res = ['INVENTORY_NUMBER', 'DATE_COMING', 'USED_MONTH', 'FIN_RESP_PERSON',
                'DEPARTMENT', 'DATE_COMISSIONING', 'ACCOUNT', 'NAME', 'CODE',
                'CARRYING_VALUE', 'COUNT', 'AMORTIZATION', 'RESIDUAL_VALUE']
    assets = pd.read_excel(file_path, header=3, usecols=cols_src)
    logging.info('finishing read')
    print(assets)
    assets.rename(columns={cols_src[i]: cols_res[i] for i in range(len(cols_src))}, inplace=True)
    logging.info('finishing rename')
    print(assets)
    assets.to_sql('assets', con=engine_decanat, if_exists='append', chunksize=10, index=False, dtype=String())
    logging.info('finishing load')


def sync_all():
    """
    Получение данных из песочницы
    :return:
    """
    sess_decanat = SessionLocal()
    sess_tezis = SessionTezis()
    conn_tezis = sess_tezis.bind.connect()
    for i in sess_tezis.query(OracleView).filter(OracleView.to_load == 1).all():
        src_table = TABS[i.table_name][1]
        dest_table = TABS[i.table_name][0]
        del_stmt = dest_table.delete()
        ins_stmt = dest_table.insert()
        res = sess_decanat.bind.execute(select([src_table]))
        conn_tezis.execute(del_stmt)
        conn_tezis.execute(ins_stmt, [i._mapping for i in res])


if __name__ == "__main__":
    sync_all()
