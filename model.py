# -*- coding: utf-8 -*-
from pydantic import BaseModel
from typing import Optional


class Document(BaseModel):
    header: str
    payload: Optional[str] = None


class String(BaseModel):
    data: str


class Application(BaseModel):
    user_guid: str
    json_data: str
    id_datatype: int


class EpguDocument(BaseModel):
    user_guid: str
    json_data: str
    id_documenttype: int
    