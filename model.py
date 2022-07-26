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


class SsoLkDatum(BaseModel):
    agree: Optional[str]
    agree_date: Optional[str]
    app_number: str
    changed: str
    code_status: str
    comment: str
    created: str
    education_form: str
    education_level: str
    education_source: str
    entrant_fullname: str
    entrant_snils: str
    id: int
    id_campaign: int
    id_competitive_group: int
    id_status: int
    name_status: str
    need_hostel: str
    registration_date: str
    uid: str
    uid_epgu: str


class SsoResultsTo(BaseModel):
    err_msg: Optional[str]
    pk: int
    processed: int




class SetCompetition(BaseModel): #epgu_ss_pkg.set_competition
    fk_abit_card: int
    fk_competition: int
    egpu_id: int
    id_jwt: int
    fk_abit_competition: int
    comp_uid: str
    guid: str

class UpdateEducData(BaseModel):#epgu_ss_pkg.update_educ_data
    fk_abit_card: int
    serial: str
    number: str
    org: str
    date: str
    d_type: int
    is_checked: int

class SetCard(BaseModel):#ac_pkg.set_card
    pk: int
    fk_student: int
    tabnum: int
    family_name: str
    name: str
    patronymic_name: str
    birthday: str
    sex: int
    year_education: int
    school: str
    ed_document_serial: str
    ed_document_number: str
    in_date_education: int
    ATT_FAMILY: str
    h_n_e: int
    accept_date: str
    passport_who_distribute: str
    passport_date_distribute: str
    pasport_number: str
    pasport_serial: str
    kod_podr: str
    place_of_birth: str
    enrolment_address: str
    enrolment_address_code: str
    enrolment_address_phone: str
    EMAIL: str
    MOBILE_PHONE: str
    insurance_num: str
    date_educ: str
