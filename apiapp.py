# -*- coding: utf-8 -*-
from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional
from logging.config import dictConfig

from config import LOG
from signer import get_jwt, to_base64_string


class Document(BaseModel):
    header: str
    payload: Optional[str] = None

dictConfig(LOG)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "API для подписи для СС"}


@app.post("/api/create-base64")
def create_item(data: str = Body(..., embed=True)) -> str:
    data_base64 = to_base64_string(data)
    return {"data_base64": data_base64}


@app.post("/api/create-jwt")
def read_item(doc: Document) -> str:
    jwt = get_jwt(header=doc.header, payload=doc.payload)
    return {"jwt": jwt}