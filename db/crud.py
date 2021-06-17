# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session

from . import models, schemas


def get_subdivision_org(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_subdivisionorg_2021).offset(skip).limit(limit).all()


def get_education_program(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_educationprogram_2021).offset(skip).limit(limit).all()


def get_campaign(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_campaign_2021).offset(skip).limit(limit).all()


def get_cmp_achievement(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_ss_cmpachievement).offset(skip).limit(limit).all()


def get_admission_volume(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_admissionvolume_2021).offset(skip).limit(limit).all()


def get_distributed_admission_volume(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_distadmissionvolume_2021).offset(skip).limit(limit).all()


def get_competitive_group(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_competitivegroup_2021).offset(skip).limit(limit).all()


def get_competitive_group_program(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_competitivegrouppr_2021).offset(skip).limit(limit).all()


def get_competitive_benefit(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_competitivebenefit_2021).offset(skip).limit(limit).all()


def get_entrance_test(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_entrancetest_2021).offset(skip).limit(limit).all()


def get_entrance_test_benefit(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_entrancetestbenefit_2021).offset(skip).limit(limit).all()


def get_entrance_test_location(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_entrancetestloc_2021).offset(skip).limit(limit).all()


def get_terms_admission(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_vw_ss_termsadmission_2021_189).offset(skip).limit(limit).all()
