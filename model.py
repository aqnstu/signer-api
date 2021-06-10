# -*- coding: utf-8 -*-
from pydantic import BaseModel
from typing import Optional


class Document(BaseModel):
    header: str
    payload: Optional[str] = None
    
class String(BaseModel):
    data: str