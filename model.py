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


class EpguJwt(BaseModel):
    id: int
    id_datatype: int
    data_json: str
    user_guid: Optional[str]
    app_number: Optional[str]


class EpguAchievement(BaseModel):
    id: int
    id_jwt_epgu: int
    data_json: str
    app_number: str
    uid_epgu: str
    id_category: int


class EpguBenefit(BaseModel):
    id: int
    id_jwt_epgu: int
    data_json: str
    app_number: str
    uid_epgu: str
    id_benefit: int


class EpguDoc(BaseModel):
    id: int
    data_json: str
    user_guid: str
    uid_epgu: str
    id_document_version: int


class EpguIdentification(BaseModel):
    id: int
    data_json: str
    user_guid: str
    uid_epgu: str
    id_document_type: int


class EpguPhoto(BaseModel):
    id: int
    data_json: str
    user_guid: str
    uid_epgu: str


class EpguTargetContract(BaseModel):
    id: int
    data_json: str
    user_guid: str
    uid_epgu: str
    uid_target_organization: str


class SsApplicationOutError(BaseModel):
    uid: str
    guid: Optional[str]
    uididentification: Optional[str]
    uideducation: Optional[str]
    issuccess: int
    msg: Optional[str]


class Status(BaseModel):
    pk: int
    is_processed: int
    err_msg: str


class MinioPath(BaseModel):
    bucket_name: str
    id_minio: str
