# -*- coding: utf-8 -*-
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, List

from db import crud
from db.database import SessionLocal, send_xlsx
from logger import CustomizeLogger
import logging.config
from model import (
    Document,
    MinioPath,
    String,
    Application,
    EpguDocument,
    EpguAchievement,
    Status,
    MinioPath,
)
from sms.sms import get_balance, get_number_available, send_sms, get_sms_state
from utils.decorators import get_original_docstring
import utils.loading
import utils.signer



def create_app() -> FastAPI:
    """
    Создать приложение FastAPI.
    """
    app = FastAPI(title="Signer API", debug=False)
    logger = CustomizeLogger.make_logger()
    app.logger = logger

    return app


app = create_app()


def get_db():
    """
    Получить сессию БД.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root() -> Dict[str, str]:
    """
    Домашняя страница :)
    """
    return {
        "message": "API для подписи и получения"
        "данных для работы с суперсервисом [Поступи онлайн]"
    }


@app.post("/api/utils/create-base64")
def create_base64(s: String) -> Dict[str, str]:
    """Получить строку Base64 из обычной строки."""
    data_base64 = utils.signer.to_base64_string(s.data)
    return {"data_base64": data_base64}


@app.post("/api/utils/create-jwt")
@get_original_docstring(utils.signer.get_jwt)
def create_jwt(doc: Document) -> Dict[str, str]:
    jwt = utils.signer.get_jwt(header=doc.header, payload=doc.payload)
    return {"jwt": jwt}


@app.get("/api/db/get-subdivision-org")
def read_subdivision_org(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    try:
        data = crud.get_subdivision_org(db, skip=skip, limit=limit)
        return data
    except Exception as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=500, detail="Database error")


@app.get("/api/db/get-education-program")
def read_education_program(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    try:
        data = crud.get_education_program(db, skip=skip, limit=limit)
        return data
    except Exception as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=500, detail="Database error")


@app.get("/api/db/get-campaign")
def read_campaign(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    data = crud.get_campaign(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-cmp-achievement")
def read_cmp_achievement(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    data = crud.get_cmp_achievement(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-admission-volume")
def read_admission_volume(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    data = crud.get_admission_volume(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-distributed-admission-volume")
def read_distributed_admission_volume(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    data = crud.get_distributed_admission_volume(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-competitive-group")
def read_competitive_group(
    skip: int = 0, limit: int = 200, db: Session = Depends(get_db)
):
    data = crud.get_competitive_group(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-competitive-group-program")
def read_competitive_group_program(
    skip: int = 0, limit: int = 200, db: Session = Depends(get_db)
):
    data = crud.get_competitive_group_program(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-competitive-benefit")
def read_competitive_benefit(
    skip: int = 0, limit: int = 200, db: Session = Depends(get_db)
):
    data = crud.get_competitive_benefit(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-entrance-test")
def read_entrance_test(
    skip: int = 0, limit: int = 1000, stage: int = 1, db: Session = Depends(get_db)
):
    if stage not in (1, 2, 3):
        raise HTTPException(
            status_code=400, detail="You should use a stage value of 1, 2 or 3"
        )
    data = crud.get_entrance_test(db, skip=skip, limit=limit, stage=stage)
    return data


@app.get("/api/db/get-entrance-test-benefit")
def read_entrance_test_benefit(
    skip: int = 0, limit: int = 15000, db: Session = Depends(get_db)
):
    data = crud.get_entrance_test_benefit(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-entrance-test-location")
def read_entrance_test_location(
    skip: int = 0, limit: int = 5000, db: Session = Depends(get_db)
):
    data = crud.get_entrance_test_location(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-terms-admission")
def read_terms_admission(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    data = crud.get_terms_admission(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-epgu-application")
def read_epgu_application(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    data = crud.get_epgu_application(db, skip=skip, limit=limit)
    return data


@app.post("/api/db/insert-into-epgu-application")
def create_record_epgu_application(app: Application, db: Session = Depends(get_db)):
    return crud.insert_into_epgu_application(
        db=db,
        user_guid=app.user_guid,
        id_jwt_epgu=app.id_jwt_epgu,
        appnumber=app.appnumber,
        json_data=app.json_data,
        id_datatype=app.id_datatype,
    )


@app.get("/api/db/get-statuses-to")
def read_statuses_to(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    data = crud.get_statuses_to(db, skip=skip, limit=limit)
    return data


@app.post("/api/db/update-statuses-to")
def update_record_statuses_to(stat: Status, db: Session = Depends(get_db)):
    data = crud.update_into_statuses_to(
        db, pk=stat.pk, is_processed=stat.is_processed, err_msg=stat.err_msg
    )
    return {"status": "OK"}


@app.get("/api/db/get-epgu-document")
def read_epgu_document(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    data = crud.get_epgu_document(db, skip=skip, limit=limit)
    return data


@app.post("/api/db/insert-into-epgu-document")
def create_record_epgu_document(doc: EpguDocument, db: Session = Depends(get_db)):
    try:
        data = crud.insert_into_epgu_document(
            db,
            user_guid=doc.user_guid,
            appnumber=doc.appnumber,
            id_jwt_epgu=doc.id_jwt_epgu,
            json_data=doc.json_data,
            id_documenttype=doc.id_documenttype,
        )
    except Exception as e:
        app.logger.error(e)
        data = None
        raise HTTPException(status_code=500, detail="DB error")
    return data


@app.get("/api/db/get-epgu-achievement")
def read_epgu_achievement(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    data = crud.get_epgu_achievement(db, skip=skip, limit=limit)
    return data


@app.post("/api/db/insert-into-epgu-achievement")
def create_record_epgu_achievement(ach: EpguAchievement, db: Session = Depends(get_db)):
    try:
        data = crud.insert_into_epgu_achievement(
            db,
            user_guid=ach.user_guid,
            appnumber=ach.appnumber,
            id_jwt_epgu=ach.id_jwt_epgu,
            json_data=ach.json_data,
            id_category=ach.id_category,
        )
    except Exception as e:
        app.logger.error(e)
        data = None
        raise HTTPException(status_code=500, detail="DB error")
    return data


@app.get("/api/db/get-competitive-group-applications-list")
def read_competitive_group_applications_list(
    competitive_group: int = None,
    skip: int = 0,
    limit: int = 40000,
    db: Session = Depends(get_db),
):
    data = crud.get_competitive_group_applications_list(
        db, competitive_group=competitive_group, skip=skip, limit=limit
    )
    return data


@app.post("/api/minio/sign")
def sign_and_upload_back_to_minio(path: MinioPath) -> Dict[str, str]:
    """
    Подписать файл из Minio и выгрузить подпись рядом с файлом.
    """
    file_name = utils.loading.download(path.bucket_name, path.id_minio)
    file_name_sign = utils.signer.sign_file(file_name)
    app.logger.error(file_name_sign)
    minio_id_sign = utils.loading.upload(
        path.bucket_name, path.id_minio, file_name_sign
    )
    return minio_id_sign


@app.get("/moby_balance")
def get_available_balance():
    """
    Получить баланс.
    """
    data = get_balance()

    return data


@app.get("/moby_number_available")
def get_number_available_sms():
    """
    Получить количество доступных СМС для отправки.
    """
    data = get_number_available()

    return data


@app.get("/moby")
def send_sms_to_phone(phone: str, text: str):
    """
    Отправить сообщение адресату ("GET" API).
    """
    data = send_sms(phone, text)
    data_parsed = str(data.get("id_sms")) if data.get("id_sms", False) else data.get("msg")

    return data_parsed


@app.post("/moby_state")
def get_sms_state_by_id(id_sms: int):
    """
    Получить статус SMS.
    """
    data = get_sms_state(id_sms)
    data_parsed = data.get("status") if data.get("status", False) else data.get("msg")

    return data_parsed


@app.get("/send_xlsx")
def get_send_xlsx(stored_proc: str, filter_str: str, params: str, columns: str, userid: int, sid: int):
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
    # вызываем хранимую процедуру с параметрами
    # генерируем excel файл
    # получаем адрес электронной почты
    # отправляем файл на этот адрес
    send_xlsx(stored_proc, filter_str, params, columns, userid, sid)

