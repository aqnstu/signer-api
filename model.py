# -*- coding: utf-8 -*-
from pydantic import BaseModel
from typing import Optional


class Document(BaseModel):
    header: str
    payload: Optional[str] = None


class String(BaseModel):
    data: str


class Application(BaseModel):
    user_guid: Optional[str] = None
    appnumber: int
    id_jwt_epgu: int
    json_data: str
    id_datatype: int


class EpguDocument(BaseModel):
    user_guid: str
    appnumber: int
    id_jwt_epgu: int
    json_data: str
    id_documenttype: int


class EpguAchievement(BaseModel):
    user_guid: str
    appnumber: int
    id_jwt_epgu: int
    json_data: str
    id_category: int


class Status(BaseModel):
    pk: int
    is_processed: int
    err_msg: str


class MinioPath(BaseModel):
    bucket_name: str
    id_minio: str
