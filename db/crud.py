# -*- coding: utf-8 -*-
from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models


def get_org_direction(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_orgdirection).offset(skip).limit(limit).all()


def get_campaign(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_campaign).offset(skip).limit(limit).all()


def get_terms_admission(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_termsadmission).offset(skip).limit(limit).all()


def get_campaign_achievement(db: Session, skip: int = 0, limit: int = 250):
    return db.query(models.t_vw_ss_achievments).offset(skip).limit(limit).all()


def get_admission_volume(db: Session, skip: int = 0, limit: int = 500):
    return db.query(models.t_vw_ss_admissionvolume_2022).offset(skip).limit(limit).all()


def get_distributed_admission_volume(db: Session, skip: int = 0, limit: int = 500):
    return (
        db.query(models.t_vw_ss_distadmissionvolume_2022)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_competitive_group(db: Session, skip: int = 0, limit: int = 500):
    return (
        db.query(models.t_vw_ss_competitivegroup_2022).offset(skip).limit(limit).all()
    )


def get_entrance_test(db: Session, skip: int = 0, limit: int = 5000, stage: int = 1):
    if stage == 1:
        return (
            db.query(models.t_tvw_ss_entrancetest_2022)
            .filter(
                models.t_tvw_ss_entrancetest_2022.c.isege == 1,
                models.t_tvw_ss_entrancetest_2022.c.uidreplaceentrancetest == None,
            )
            .order_by(
                models.t_tvw_ss_entrancetest_2022.c.uidcompetitivegroup,
                models.t_tvw_ss_entrancetest_2022.c.priority,
            )
            .offset(skip)
            .limit(limit)
            .all()
        )
    if stage == 2:
        return (
            db.query(models.t_tvw_ss_entrancetest_2022)
            .filter(
                models.t_tvw_ss_entrancetest_2022.c.isege == 1,
                models.t_tvw_ss_entrancetest_2022.c.uidreplaceentrancetest != None,
            )
            .order_by(
                models.t_tvw_ss_entrancetest_2022.c.uidcompetitivegroup,
                models.t_tvw_ss_entrancetest_2022.c.priority,
            )
            .offset(skip)
            .limit(limit)
            .all()
        )
    if stage == 3:
        return (
            db.query(models.t_tvw_ss_entrancetest_2022)
            .filter(models.t_tvw_ss_entrancetest_2022.c.isege == 0)
            .order_by(
                models.t_tvw_ss_entrancetest_2022.c.uidcompetitivegroup,
                models.t_tvw_ss_entrancetest_2022.c.priority,
            )
            .offset(skip)
            .limit(limit)
            .all()
        )


def get_entrance_test_location(db: Session, skip: int = 0, limit: int = 500000):
    return db.query(models.t_vw_ss_entrancetestlocation).offset(skip).limit(limit).all()


def insert_into_epgu_application(
    db: Session,
    appnumber: int,
    id_jwt_epgu: int,
    json_data: str,
    id_datatype: int,
    user_guid: str = None,
):
    row = models.SsEpguapplication(
        epgu_id=user_guid,
        epgu_application_id=appnumber,
        id_jwt=id_jwt_epgu,
        json=json_data,
        id_ss_entity_type=id_datatype,
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


def get_epgu_document(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SsEpgudocument).offset(skip).limit(limit).all()


def get_competitive_group_applications_list(
    db: Session,
    competitive_group: int = None,
    skip: int = 0,
    limit: int = 40000,
):
    if not competitive_group:
        return (
            db.query(models.t_vw_ss_comp_applist_2021).offset(skip).limit(limit).all()
        )
    else:
        return (
            db.query(models.t_vw_ss_comp_applist_2021)
            .filter(
                models.t_vw_ss_comp_applist_2021.c.UIDCompetitiveGroup
                == competitive_group
            )
            .offset(skip)
            .limit(limit)
            .all()
        )


def get_epgu_jwt(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SsoJwtEpgu).offset(skip).limit(limit).all()


def insert_into_epgu_jwt(
    db: Session,
    id: str,
    id_datatype: int,
    data_json: str,
    user_guid: str,
    app_number: str,
):
    if (
        not db.query(models.SsoJwtEpgu)
        .filter(
            models.SsoJwtEpgu.user_guid == user_guid,
            models.SsoJwtEpgu.app_number == app_number,
        )
        .one_or_none()
    ):
        row = models.SsoJwtEpgu(
            id=id,
            id_datatype=id_datatype,
            data_json=data_json,
            user_guid=user_guid,
            app_number=app_number,
        )
        db.add(row)
    else:
        db.query(models.SsoJwtEpgu).filter(
            models.SsoJwtEpgu.user_guid == user_guid,
            models.SsoJwtEpgu.app_number == app_number,
        ).update({models.SsoJwtEpgu.data_json: data_json})
    db.commit()


def get_epgu_achievement(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SsoAchievement).offset(skip).limit(limit).all()


def insert_into_epgu_achievement(
    db: Session,
    id: str,
    id_jwt_epgu: int,
    data_json: str,
    app_number: str,
    uid_epgu: int,
    id_category: int,
):
    if (
        not db.query(models.SsoAchievement)
        .filter(
            models.SsoAchievement.app_number == app_number,
            models.SsoAchievement.uid_epgu == uid_epgu,
        )
        .one_or_none()
    ):
        row = models.SsoAchievement(
            id=id,
            id_jwt_epgu=id_jwt_epgu,
            data_json=data_json,
            app_number=app_number,
            uid_epgu=uid_epgu,
            id_category=id_category,
        )
        db.add(row)
    else:
        db.query(models.SsoAchievement).filter(
            models.SsoAchievement.app_number == app_number,
            models.SsoAchievement.uid_epgu == uid_epgu,
        ).update({models.SsoAchievement.data_json: data_json})
    db.commit()


def get_epgu_benefit(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SsoBenefit).offset(skip).limit(limit).all()


def insert_into_epgu_benefit(
    db: Session,
    id: str,
    id_jwt_epgu: int,
    data_json: str,
    app_number: str,
    uid_epgu: int,
    id_benefit: int,
):
    if (
        not db.query(models.SsoBenefit)
        .filter(
            models.SsoBenefit.app_number == app_number,
            models.SsoBenefit.uid_epgu == uid_epgu,
        )
        .one_or_none()
    ):
        row = models.SsoBenefit(
            id=id,
            id_jwt_epgu=id_jwt_epgu,
            data_json=data_json,
            app_number=app_number,
            uid_epgu=uid_epgu,
            id_benefit=id_benefit,
        )
        db.add(row)
    else:
        db.query(models.SsoBenefit).filter(
            models.SsoBenefit.app_number == app_number,
            models.SsoBenefit.uid_epgu == uid_epgu,
        ).update({models.SsoBenefit.data_json: data_json})

    db.commit()


def get_epgu_doc(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SsoDoc).offset(skip).limit(limit).all()


def insert_into_epgu_doc(
    db: Session,
    id: str,
    data_json: str,
    user_guid: str,
    uid_epgu: int,
    id_document_version: int,
):
    if (
        not db.query(models.SsoDoc)
        .filter(
            models.SsoDoc.user_guid == user_guid,
            models.SsoDoc.uid_epgu == uid_epgu,
        )
        .one_or_none()
    ):
        row = models.SsoDoc(
            id=id,
            data_json=data_json,
            user_guid=user_guid,
            uid_epgu=uid_epgu,
            id_document_version=id_document_version,
        )
        db.add(row)
    else:
        db.query(models.SsoDoc).filter(
            models.SsoDoc.user_guid == user_guid,
            models.SsoDoc.uid_epgu == uid_epgu,
        ).update({models.SsoDoc.data_json: data_json})

    db.commit()


def get_epgu_identification(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SsoIdentification).offset(skip).limit(limit).all()


def insert_into_epgu_identification(
    db: Session,
    id: str,
    data_json: str,
    user_guid: str,
    uid_epgu: int,
    id_document_type: int,
):
    if (
        not db.query(models.SsoIdentification)
        .filter(
            models.SsoIdentification.user_guid == user_guid,
            models.SsoIdentification.uid_epgu == uid_epgu,
        )
        .one_or_none()
    ):
        row = models.SsoIdentification(
            id=id,
            data_json=data_json,
            user_guid=user_guid,
            uid_epgu=uid_epgu,
            id_document_type=id_document_type,
        )
        db.add(row)
    else:
        db.query(models.SsoIdentification).filter(
            models.SsoIdentification.user_guid == user_guid,
            models.SsoIdentification.uid_epgu == uid_epgu,
        ).update({models.SsoIdentification.data_json: data_json})

    db.commit()


def get_epgu_photo(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SsoPhoto).offset(skip).limit(limit).all()


def insert_into_epgu_photo(
    db: Session,
    id: str,
    data_json: str,
    user_guid: str,
    uid_epgu: int,
):
    if (
        not db.query(models.SsoPhoto)
        .filter(
            models.SsoPhoto.user_guid == user_guid,
            models.SsoPhoto.uid_epgu == uid_epgu,
        )
        .one_or_none()
    ):
        row = models.SsoPhoto(
            id=id,
            data_json=data_json,
            user_guid=user_guid,
            uid_epgu=uid_epgu,
        )
        db.add(row)
    else:
        db.query(models.SsoPhoto).filter(
            models.SsoPhoto.user_guid == user_guid,
            models.SsoPhoto.uid_epgu == uid_epgu,
        ).update({models.SsoPhoto.data_json: data_json})

    db.commit()


def get_epgu_target_organization(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SsoTargetContract).offset(skip).limit(limit).all()


def insert_into_epgu_target_contract(
    db: Session,
    id: str,
    data_json: str,
    user_guid: str,
    uid_epgu: int,
    uid_target_organization: int,
):
    if (
        not db.query(models.SsoTargetContract)
        .filter(
            models.SsoTargetContract.user_guid == user_guid,
            models.SsoTargetContract.uid_epgu == uid_epgu,
        )
        .one_or_none()
    ):
        row = models.SsoTargetContract(
            id=id,
            data_json=data_json,
            user_guid=user_guid,
            uid_epgu=uid_epgu,
            uid_target_organization=uid_target_organization,
        )
        db.add(row)
    else:
        db.query(models.SsoTargetContract).filter(
            models.SsoTargetContract.user_guid == user_guid,
            models.SsoTargetContract.uid_epgu == uid_epgu,
        ).update({models.SsoTargetContract.data_json: data_json})

    db.commit()


def get_statuses_to(db: Session, skip: int = 0, limit: int = 5000):
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


def get_table_by_name(db: Session, table: str, field_name: str = '', field_value: str = ''):
    if not isinstance(table, str) or not isinstance(field_name, str) or not isinstance(field_value, str) or \
            len(table.split()) > 1 or len(field_name.split()) > 1 or len(field_value.split()) > 1:
        return {"msg": "bad params"}

    query = f"SELECT * FROM abituser.{table}"
    where = "" if not field_name or not field_value else f" where {field_name} = {field_value}"
    return db.execute(query + where).fetchall()
