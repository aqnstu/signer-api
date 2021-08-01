# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session

from . import models, schemas


def get_subdivision_org(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_subdivisionorg_2021).offset(skip).limit(limit).all()


def get_education_program(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.t_vw_ss_educationprogram_2021).offset(skip).limit(limit).all()
    )


def get_campaign(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_campaign_2021).offset(skip).limit(limit).all()


def get_cmp_achievement(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_ss_cmpachievement).offset(skip).limit(limit).all()


def get_admission_volume(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_admissionvolume_2021).offset(skip).limit(limit).all()


def get_distributed_admission_volume(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.t_vw_ss_distadmissionvolume_2021)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_competitive_group(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.t_vw_ss_competitivegroup_2021).offset(skip).limit(limit).all()
    )


def get_competitive_group_program(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.t_vw_ss_competitivegrouppr_2021).offset(skip).limit(limit).all()
    )


def get_competitive_benefit(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.t_vw_ss_competitivebenefit_2021).offset(skip).limit(limit).all()
    )


def get_entrance_test(db: Session, skip: int = 0, limit: int = 100, stage: int = 1):
    if stage == 1:
        return (
            db.query(models.t_vw_ss_entrancetest_2021)
            .filter(
                models.t_vw_ss_entrancetest_2021.c.IsEge == 1,
                models.t_vw_ss_entrancetest_2021.c.UIDReplaceEntranceTest == None,
            )
            .offset(skip)
            .limit(limit)
            .all()
        )
    if stage == 2:
        return (
            db.query(models.t_vw_ss_entrancetest_2021)
            .filter(
                models.t_vw_ss_entrancetest_2021.c.IsEge == 1,
                models.t_vw_ss_entrancetest_2021.c.UIDReplaceEntranceTest != None,
            )
            .offset(skip)
            .limit(limit)
            .all()
        )
    if stage == 3:
        return (
            db.query(models.t_vw_ss_entrancetest_2021)
            .filter(models.t_vw_ss_entrancetest_2021.c.IsEge == 0)
            .offset(skip)
            .limit(limit)
            .all()
        )


def get_entrance_test_benefit(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.t_vw_ss_entrancetestbenefit_2021)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_entrance_test_location(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_entrancetestloc_2021).offset(skip).limit(limit).all()


def get_terms_admission(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_ss_termsadmission).offset(skip).limit(limit).all()


def get_epgu_application(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SsEpguapplication).offset(skip).limit(limit).all()


def insert_into_epgu_application(
    db: Session, appnumber: int, id_jwt_epgu: int,  json_data: str, id_datatype: int, user_guid: str = None
):
    row = models.SsEpguapplication(
        epgu_id=user_guid,
        epgu_application_id=appnumber,
        id_jwt=id_jwt_epgu,
        json=json_data,
        id_ss_entity_type=id_datatype
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


def get_statuses_to(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.SsStatusesTo)
        .filter(models.SsStatusesTo.is_processed == 0)
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_into_statuses_to(
    db: Session, pk: int, is_processed: int, err_msg: str = None
):
    db.query(models.SsStatusesTo).filter(models.SsStatusesTo.pk == pk).update(
        {
            models.SsStatusesTo.is_processed: is_processed,
            models.SsStatusesTo.err_msg: err_msg,
        }
    )
    db.commit()


def get_epgu_document(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SsEpgudocument).offset(skip).limit(limit).all()


def insert_into_epgu_document(
    db: Session, user_guid: str, appnumber: int, id_jwt_epgu:int, json_data: str, id_documenttype: int
):
    row = models.SsEpgudocument(
        epgu_id=user_guid,
        epgu_application_id=appnumber,
        id_jwt=id_jwt_epgu,
        json=json_data,
        id_ss_documenttype=id_documenttype
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


def get_epgu_achievement(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SsEpguachievement).offset(skip).limit(limit).all()


def insert_into_epgu_achievement(
    db: Session, user_guid: str, appnumber: int, id_jwt_epgu: int, json_data: str, id_category: int
):
    row = models.SsEpguachievement(
        epgu_id=user_guid,
        epgu_application_id=appnumber,
        id_jwt=id_jwt_epgu,
        json=json_data,
        id_ss_category=id_category
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


def get_competitive_group_applications_list(db: Session, skip: int = 0, limit: int = 40000):
    return db.query(models.t_vw_ss_comp_applist_2021).offset(skip).limit(limit).all()