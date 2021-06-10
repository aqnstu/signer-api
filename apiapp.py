# -*- coding: utf-8 -*-
from fastapi import Depends, FastAPI, HTTPException, Body
from sqlalchemy.orm import Session
import logging.config
# import uvicorn

from db import crud, models, schemas
from db.database import SessionLocal, engine
from logger import CustomizeLogger
from model import Document
from signer import get_jwt, to_base64_string


def create_app() -> FastAPI:
    app = FastAPI(title="Signer API", debug=False)
    logger = CustomizeLogger.make_logger()
    app.logger = logger

    return app


app = create_app()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "API для подписи для СС"}


@app.post("/api/utils/create-base64")
def create_item(data: str = Body(..., embed=True)) -> str:
    data_base64 = to_base64_string(data)
    return {"data_base64": data_base64}


@app.post("/api/utils/create-jwt")
def read_item(doc: Document) -> str:
    jwt = get_jwt(header=doc.header, payload=doc.payload)
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
def read_subdivision_org(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    try:
        data = crud.get_education_program(db, skip=skip, limit=limit)
        return data
    except Exception as e:
        logging.error(e, exc_info=True)
        raise HTTPException(status_code=500, detail="Database error")


@app.get("/api/db/get-campaign")
def read_subdivision_org(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    data = crud.get_campaign(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-cmp-achievement")
def read_subdivision_org(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    data = crud.get_cmp_achievement(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-admission-volume")
def read_subdivision_org(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    data = crud.get_admission_volume(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-distributed-admission-volume")
def read_subdivision_org(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    data = crud.get_distributed_admission_volume(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-competitive-group")
def read_subdivision_org(
    skip: int = 0, limit: int = 200, db: Session = Depends(get_db)
):
    data = crud.get_competitive_group(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-competitive-group-program")
def read_subdivision_org(
    skip: int = 0, limit: int = 200, db: Session = Depends(get_db)
):
    data = crud.get_competitive_group_program(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-competitive-benefit")
def read_subdivision_org(
    skip: int = 0, limit: int = 200, db: Session = Depends(get_db)
):
    data = crud.get_competitive_benefit(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-entrance-test")
def read_subdivision_org(
    skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)
):
    data = crud.get_entrance_test(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-entrance-test-benefit")
def read_subdivision_org(
    skip: int = 0, limit: int = 15000, db: Session = Depends(get_db)
):
    data = crud.get_entrance_test_benefit(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-entrance-test-location")
def read_subdivision_org(
    skip: int = 0, limit: int = 5000, db: Session = Depends(get_db)
):
    data = crud.get_entrance_test_location(db, skip=skip, limit=limit)
    return data


@app.get("/api/db/get-terms-admission")
def read_subdivision_org(
    skip: int = 0, limit: int = 5000, db: Session = Depends(get_db)
):
    data = crud.get_terms_admission(db, skip=skip, limit=limit)
    return data
