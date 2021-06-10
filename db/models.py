# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, Integer, Table, Text, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class SsAchievementcategory(Base):
    __tablename__ = "ss_achievementcategories"
    __table_args__ = {"comment": "Категории индивидуальных достижений"}

    id = Column(Integer, primary_key=True)
    Actual = Column(Integer)
    Name = Column(VARCHAR(500))


t_ss_admissionvolume = Table(
    "ss_admissionvolume",
    metadata,
    Column(
        "UID",
        NUMBER(asdecimal=False),
        comment="Уникальный идентификатор записи КЦП ООВО",
    ),
    Column(
        "UIDCampaign",
        NUMBER(asdecimal=False),
        comment="Уникальный идентификатор приемной кампании ООВО",
    ),
    Column(
        "IDDirection",
        Integer,
        comment="Идентификатор направления подготовки – содержит ссылку на id справочника Directions",
    ),
    Column(
        "IDEducationLevel",
        NUMBER(asdecimal=False),
        comment="Идентификатор уровня образования – содержит ссылку на id справочника educationLevel",
    ),
    Column("name", VARCHAR(1000), comment="Имя по ОКСО (не используется в выгрузке)"),
    Column(
        "Budget_o", NUMBER(asdecimal=False), comment="Значение в разрезе бюджет/очно"
    ),
    Column(
        "Budget_oz",
        NUMBER(asdecimal=False),
        comment="Значение в разрезе бюджет/очно-заочно",
    ),
    Column(
        "Budget_z", NUMBER(asdecimal=False), comment="Значение в разрезе бюджет/заочно"
    ),
    Column("Quota_o", NUMBER(asdecimal=False), comment="Значение в разрезе квота/очно"),
    Column(
        "Quota_oz",
        NUMBER(asdecimal=False),
        comment="Значение в разрезе квота/очно-заочно",
    ),
    Column(
        "Quota_z", NUMBER(asdecimal=False), comment="Значение в разрезе квота/заочно"
    ),
    Column("Paid_o", NUMBER(asdecimal=False), comment="Значение в разрезе платно/очно"),
    Column(
        "Paid_oz",
        NUMBER(asdecimal=False),
        comment="Значение в разрезе платно/очно-заочно",
    ),
    Column(
        "Paid_z", NUMBER(asdecimal=False), comment="Значение в разрезе платно/заочно"
    ),
    Column(
        "Target_o", NUMBER(asdecimal=False), comment="Значение в разрезе целевое/очно"
    ),
    Column(
        "Target_oz",
        NUMBER(asdecimal=False),
        comment="Значение в разрезе целевое/очно-заочно",
    ),
    Column(
        "Target_z", NUMBER(asdecimal=False), comment="Значение в разрезе целевое/заочно"
    ),
    comment="Контрольные цифры приема ",
)


class SsAppealstatus(Base):
    __tablename__ = "ss_appealstatuses"
    __table_args__ = {"comment": "Статус апелляции"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(50))


class SsApplicationstatus(Base):
    __tablename__ = "ss_applicationstatuses"
    __table_args__ = {"comment": "Статусы заявлений"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    code = Column(VARCHAR(100))
    name = Column(VARCHAR(200))


class SsBenefit(Base):
    __tablename__ = "ss_benefits"
    __table_args__ = {"comment": "Справочник льгот"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(200))
    shortname = Column(VARCHAR(100))


t_ss_campaign = Table(
    "ss_campaign",
    metadata,
    Column("UID", NUMBER(asdecimal=False)),
    Column("Name", VARCHAR(276)),
    Column("YearStart", NUMBER(asdecimal=False)),
    Column("YearEnd", NUMBER(asdecimal=False)),
    Column("IDEducationForm1", NUMBER(asdecimal=False)),
    Column("IDEducationForm2", NUMBER(asdecimal=False)),
    Column("IDEducationLevel1", NUMBER(asdecimal=False)),
    Column("IDEducationLevel2", NUMBER(asdecimal=False)),
    Column("IDCampaignType", NUMBER(asdecimal=False)),
    Column("IDCampaignStatus", NUMBER(asdecimal=False)),
    Column("NumberAgree", NUMBER(asdecimal=False)),
    Column("CountDirections", NUMBER(asdecimal=False)),
    Column("EndDate", VARCHAR(26)),
)


class SsCampaignstatus(Base):
    __tablename__ = "ss_campaignstatuses"
    __table_args__ = {"comment": "Статус приемной кампании"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(200))
    code = Column(VARCHAR(50))


t_ss_campaigntypes = Table(
    "ss_campaigntypes",
    metadata,
    Column("id", Integer),
    Column("actual", NUMBER(1, 0, False)),
    Column("name", VARCHAR(200)),
    comment="Тип приемной кампании",
)


t_ss_cmpachievement = Table(
    "ss_cmpachievement",
    metadata,
    Column(
        "UIDCampaign",
        Integer,
        comment="Уникальный идентификатор приемной кампании ООВО",
    ),
    Column(
        "UID",
        Integer,
        comment="Уникальный идентификатор индивидуального достижения ООВО",
    ),
    Column(
        "IDCategory",
        Integer,
        comment="Идентификатор категории индивидуального достижения – содержит ссылку на id справочника achievementCategory",
    ),
    Column("Name", VARCHAR(500), comment="Наименование индивидуального достижения"),
    Column("MaxValue", Integer, comment="Балл"),
    comment="Индивидуальные достижения, учитываемые в рамках приемной кампании",
)


class SsCompatriotcategory(Base):
    __tablename__ = "ss_compatriotcategories"
    __table_args__ = {"comment": "Категории соотечественников"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(200))


t_ss_competitivegroup = Table(
    "ss_competitivegroup",
    metadata,
    Column("UID", NUMBER(asdecimal=False)),
    Column("UIDCampaign", NUMBER(asdecimal=False)),
    Column("Name", VARCHAR(786)),
    Column("IDLevelBudget", NUMBER(asdecimal=False)),
    Column("IDEducationLevel", NUMBER(asdecimal=False)),
    Column("IDEducationSource", NUMBER(asdecimal=False)),
    Column("IDEducationForm", NUMBER(asdecimal=False)),
    Column("idocso", Integer),
    Column("AdmissionNumber", NUMBER(asdecimal=False)),
    Column("Comment", CHAR(1)),
)


class SsCompositiontheme(Base):
    __tablename__ = "ss_compositionthemes"
    __table_args__ = {"comment": "Темы сочинений"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(1000))
    yeartheme = Column(Integer)
    numbertheme = Column(Integer)


class SsDirection(Base):
    __tablename__ = "ss_directions"
    __table_args__ = {
        "comment": "Общероссийский классификатор специальностей по образованию"
    }

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    section = Column(Integer)
    code = Column(VARCHAR(100))
    name = Column(VARCHAR(1000))
    codemcko2011 = Column(Integer)
    codemckoO2013 = Column(Integer)
    idparent = Column(Integer)
    ideducationlevel = Column(Integer)


class SsDisabilitytype(Base):
    __tablename__ = "ss_disabilitytype"
    __table_args__ = {"comment": "Категории инвалидности"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(200))


class SsDocumentcategory(Base):
    __tablename__ = "ss_documentcategory"
    __table_args__ = {"comment": "Категории документов"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(100))


class SsDocumenttype(Base):
    __tablename__ = "ss_documenttypes"
    __table_args__ = {"comment": "Типы документов"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(1000))
    idcategory = Column(Integer)
    idsyscategory = Column(Integer)


class SsEducationform(Base):
    __tablename__ = "ss_educationforms"
    __table_args__ = {"comment": "Формы образования"}

    id = Column(Integer, primary_key=True)
    actual = Column(NUMBER(1, 0, False))
    name = Column(VARCHAR(200))


class SsEducationlevel(Base):
    __tablename__ = "ss_educationlevels"
    __table_args__ = {"comment": "Уровни образования ПК"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(200))
    code = Column(Integer)


class SsEducationsource(Base):
    __tablename__ = "ss_educationsources"
    __table_args__ = {"comment": "Источник финансирования"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(200))


class SsEdulevelscampaigntype(Base):
    __tablename__ = "ss_edulevelscampaigntypes"
    __table_args__ = {"comment": "Типы ПК по уровням образования"}

    id = Column(Integer, primary_key=True)
    idcampaigntype = Column(Integer)
    ideducationlevel = Column(Integer)


t_ss_entrancetestdocumenttype = Table(
    "ss_entrancetestdocumenttype",
    metadata,
    Column("id", Integer),
    Column("actual", Integer),
    Column("name", VARCHAR(100)),
    comment="Типы документов вступительного испытания",
)


class SsEntrancetestresultsource(Base):
    __tablename__ = "ss_entrancetestresultsources"
    __table_args__ = {"comment": "Источник результата вступительного испытания"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(200))


class SsEntrancetesttype(Base):
    __tablename__ = "ss_entrancetesttype"
    __table_args__ = {"comment": "Тип вступительного испытания"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(500))


class SsGender(Base):
    __tablename__ = "ss_genders"
    __table_args__ = {"comment": "Пол"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(50))


class SsLevelsbudget(Base):
    __tablename__ = "ss_levelsbudget"
    __table_args__ = {"comment": "Уровни бюджета"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(100))


class SsMilitarycategory(Base):
    __tablename__ = "ss_militarycategories"
    __table_args__ = {"comment": "Категории военнослужащих"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(200))


class SsMinscoresubject(Base):
    __tablename__ = "ss_minscoresubjects"
    __table_args__ = {"comment": "Минимальное значение ЕГЭ по предметам"}

    id = Column(Integer, primary_key=True)
    idsubject = Column(Integer)
    egeyear = Column(Integer)
    minscore = Column(Integer)


class SsOkcm(Base):
    __tablename__ = "ss_okcms"
    __table_args__ = {"comment": "Общероссийский классификатор стран мира"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    code = Column(Integer)
    shortname = Column(VARCHAR(100))
    fullname = Column(VARCHAR(500))
    af = Column(VARCHAR(20))
    afg = Column(VARCHAR(20))
    utvdate = Column(Text)
    vveddate = Column(Text)


class SsOktmo(Base):
    __tablename__ = "ss_oktmos"
    __table_args__ = {"comment": "Справочник муниципалитетов (из ОКТМО)"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    ter = Column(Integer)
    kod1 = Column(Integer)
    kod2 = Column(Integer)
    kod3 = Column(Integer)
    kc = Column(Integer)
    section = Column(Integer)
    name = Column(VARCHAR(500))
    utvdate = Column(Text)
    vveddate = Column(Text)


class SsOlympicdiplomatype(Base):
    __tablename__ = "ss_olympicdiplomatype"
    __table_args__ = {"comment": "Типы дипломов олимпиад"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(100))


class SsOlympiclevel(Base):
    __tablename__ = "ss_olympiclevels"
    __table_args__ = {"comment": "Уровни олимпиады задаваемые в рамках льготы"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(100))


class SsOlympicminegescore(Base):
    __tablename__ = "ss_olympicminegescores"
    __table_args__ = {"comment": "Минимальное значение ЕГЭ для подтверждения олимпиады"}

    id = Column(Integer, primary_key=True)
    egeyear = Column(Integer)
    minscore = Column(Integer)


class SsOlympicslist(Base):
    __tablename__ = "ss_olympicslist"
    __table_args__ = {"comment": "Перечень олимпиад в Сервисе приема"}

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(1000))
    ordernumber = Column(Integer)
    olympyear = Column(Integer)
    createdat = Column(Text)
    idauthor = Column(Integer)
    actual = Column(Integer)


class SsOlympicsprofile(Base):
    __tablename__ = "ss_olympicsprofiles"
    __table_args__ = {
        "comment": "Сопоставление олимпиад с профилем OlympicsProfilesList и уровнями OlympicLevels"
    }

    id = Column(Integer, primary_key=True)
    idolimpic = Column(Integer)
    idolimpiclevel = Column(Integer)
    idprofile = Column(Integer)
    createdat = Column(Text)
    idauthor = Column(Integer)
    actual = Column(Integer)


class SsOlympicsprofileslist(Base):
    __tablename__ = "ss_olympicsprofileslist"
    __table_args__ = {"comment": "Перечень профилей олимпиад в Сервисе приема"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(500))
    idauthor = Column(Integer)


class SsOlympicsprofilessubject(Base):
    __tablename__ = "ss_olympicsprofilessubjects"
    __table_args__ = {
        "comment": "Сопоставление профилей олимпиады OlympicsProfilesList с общеобразовательными предметами Subject"
    }

    id = Column(Integer, primary_key=True)
    idprofile = Column(Integer)
    idsubject = Column(Integer)


class SsOlympictype(Base):
    __tablename__ = "ss_olympictypes"
    __table_args__ = {"comment": "Типы олимпиад"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(200))


t_ss_orderadmissionstatuses = Table(
    "ss_orderadmissionstatuses",
    metadata,
    Column("id", Integer),
    Column("actual", Integer),
    Column("name", VARCHAR(100)),
    comment="Статус приказов",
)


class SsOrderadmissiontype(Base):
    __tablename__ = "ss_orderadmissiontypes"
    __table_args__ = {"comment": "Типы приказов"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(100))


t_ss_orphancategories = Table(
    "ss_orphancategories",
    metadata,
    Column("id", Integer),
    Column("name", VARCHAR(200)),
    Column("actual", Integer),
    comment="Категория документов детей-сирот",
)


t_ss_parentslostcategories = Table(
    "ss_parentslostcategories",
    metadata,
    Column("id", Integer),
    Column("actual", Integer),
    Column("name", VARCHAR(200)),
    comment="Категории граждан, родители и опекуны которых погибли при исполнении служебных обязанностей",
)


class SsRadiationworkcategory(Base):
    __tablename__ = "ss_radiationworkcategories"
    __table_args__ = {
        "comment": "Категории граждан, участвовавших в работах на радиационных объектах или подвергшихся воздействию радиации"
    }

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(200))


class SsRegion(Base):
    __tablename__ = "ss_regions"

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    code = Column(Integer)
    name = Column(VARCHAR(100))


t_ss_reit = Table("ss_reit", metadata, Column("text", Text))


class SsReturntype(Base):
    __tablename__ = "ss_returntypes"
    __table_args__ = {"comment": "Типы результата"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(200))


t_ss_sogl = Table(
    "ss_sogl",
    metadata,
    Column("uid_epgu", NUMBER(asdecimal=False)),
    Column("sogl", NUMBER(asdecimal=False)),
    Column("otzyv", NUMBER(asdecimal=False)),
    Column("comp", VARCHAR(1000)),
    Column("date_sogl", DateTime),
    Column("date_otzv", DateTime),
)


t_ss_stagesadmission = Table(
    "ss_stagesadmission",
    metadata,
    Column("id", Integer),
    Column("actual", Integer),
    Column("name", VARCHAR(200)),
    comment="Этапы зачисления",
)


class SsSubject(Base):
    __tablename__ = "ss_subjects"
    __table_args__ = {"comment": "Предметы вступительных испытаний"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(200))
    olympic = Column(Integer)
    ege = Column(Integer)


class SsTermsadmissionkind(Base):
    __tablename__ = "ss_termsadmissionkinds"
    __table_args__ = {"comment": "Виды сроков приема"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(200))
    idstagesadmission = Column(Integer)


class SsTermsadmissionmatch(Base):
    __tablename__ = "ss_termsadmissionmatches"
    __table_args__ = {
        "comment": "Сопоставление видов срока приема с уровнем обучения, формой обучения, источником финансирования и этапами зачисления согласно приказу приема текущего года."
    }

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    idtermsadmission = Column(Integer)
    ideducationlevel = Column(Integer)
    ideducationform = Column(Integer)
    ideducationsource = Column(Integer)
    year = Column(Integer)
    endevent = Column(Text)
    idstagesadmission = Column(Integer)
    startevent = Column(Text)


t_ss_test = Table(
    "ss_test",
    metadata,
    Column("snils", VARCHAR(1000)),
    Column("q", VARCHAR(1000)),
    Column("sex", NUMBER(asdecimal=False)),
    Column("f", VARCHAR(1000)),
    Column("n", VARCHAR(1000)),
    Column("p", VARCHAR(1000)),
    Column("birthday", VARCHAR(1000)),
    Column("pasp_serial", VARCHAR(1000)),
    Column("pasp_num", VARCHAR(1000)),
    Column("pasp_date", VARCHAR(1000)),
    Column("pasp_who", VARCHAR(1000)),
    Column("pasp_podr", VARCHAR(1000)),
    Column("edu_serial", VARCHAR(1000)),
    Column("edu_num", VARCHAR(1000)),
    Column("edu_org", VARCHAR(1000)),
    Column("edu_date", VARCHAR(1000)),
    Column("reg_adress", VARCHAR(1000)),
    Column("birthplace", VARCHAR(1000)),
    Column("email", VARCHAR(1000)),
    Column("phone", VARCHAR(1000)),
    Column("accept_date", VARCHAR(1000)),
    Column("id_app_status", VARCHAR(1000)),
    Column("comp", VARCHAR(1000)),
    Column("app_number", NUMBER(asdecimal=False)),
    Column("date_load", DateTime),
    Column("fk_abit_card", NUMBER(asdecimal=False)),
    Column("need_hostel", NUMBER(asdecimal=False)),
    Column("nh", VARCHAR(1000)),
)


t_ss_try = Table(
    "ss_try",
    metadata,
    Column("q", NUMBER(asdecimal=False)),
    Column("w", NUMBER(asdecimal=False)),
    Column("e", NUMBER(asdecimal=False)),
    Column("r", NUMBER(asdecimal=False)),
    Column("t", NUMBER(asdecimal=False)),
    Column("y", NUMBER(asdecimal=False)),
)


class SsVeterancategory(Base):
    __tablename__ = "ss_veterancategories"
    __table_args__ = {"comment": "Категории граждан, участвовавших в боевых действиях"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(200))


class SsViolationtype(Base):
    __tablename__ = "ss_violationtypes"
    __table_args__ = {"comment": "Тип нарушений в заявлении"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(100))


t_vw_ss_admissionvolume_2021 = Table(
    "vw$ss_admissionvolume_2021",
    metadata,
    Column("UID", NUMBER(asdecimal=False)),
    Column("UIDCampaign", NUMBER(asdecimal=False)),
    Column("IDDirection", Integer, nullable=False),
    Column("IDEducationLevel", NUMBER(asdecimal=False)),
    Column("name", VARCHAR(1000)),
    Column("Budget_o", NUMBER(asdecimal=False)),
    Column("Budget_oz", NUMBER(asdecimal=False)),
    Column("Budget_z", NUMBER(asdecimal=False)),
    Column("Quota_o", NUMBER(asdecimal=False)),
    Column("Quota_oz", NUMBER(asdecimal=False)),
    Column("Quota_z", NUMBER(asdecimal=False)),
    Column("Paid_o", NUMBER(asdecimal=False)),
    Column("Paid_oz", NUMBER(asdecimal=False)),
    Column("Paid_z", NUMBER(asdecimal=False)),
    Column("Target_o", NUMBER(asdecimal=False)),
    Column("Target_oz", NUMBER(asdecimal=False)),
    Column("Target_z", NUMBER(asdecimal=False)),
)


t_vw_ss_campaign_2021 = Table(
    "vw$ss_campaign_2021",
    metadata,
    Column("UID", NUMBER(asdecimal=False)),
    Column("Name", VARCHAR(276)),
    Column("YearStart", NUMBER(asdecimal=False)),
    Column("YearEnd", NUMBER(asdecimal=False)),
    Column("IDEducationForm1", NUMBER(asdecimal=False)),
    Column("IDEducationForm2", NUMBER(asdecimal=False)),
    Column("IDEducationLevel1", NUMBER(asdecimal=False)),
    Column("IDEducationLevel2", NUMBER(asdecimal=False)),
    Column("IDCampaignType", NUMBER(asdecimal=False)),
    Column("IDCampaignStatus", NUMBER(asdecimal=False)),
    Column("NumberAgree", NUMBER(asdecimal=False)),
    Column("CountDirections", NUMBER(asdecimal=False)),
    Column("EndDate", VARCHAR(26)),
)


t_vw_ss_competitivebenefit_2021 = Table(
    "vw$ss_competitivebenefit_2021",
    metadata,
    Column("UIDCompetitiveGroup", NUMBER(asdecimal=False)),
    Column("IDBenefit", NUMBER(asdecimal=False)),
    Column("IDOlympicDiplomaType", NUMBER(asdecimal=False)),
    Column("EgeMinValue", NUMBER(asdecimal=False)),
    Column("IDOlympicType", NUMBER(asdecimal=False)),
    Column("IDOlympicLevels", NUMBER(asdecimal=False)),
    Column("OlympicProfiles", VARCHAR(0)),
    Column("UID", NUMBER(asdecimal=False)),
    Column("fk_competition", NUMBER(asdecimal=False)),
)


t_vw_ss_competitivegroup_2021 = Table(
    "vw$ss_competitivegroup_2021",
    metadata,
    Column("UID", NUMBER(asdecimal=False)),
    Column("UIDCampaign", NUMBER(asdecimal=False)),
    Column("Name", VARCHAR(801)),
    Column("IDLevelBudget", NUMBER(asdecimal=False)),
    Column("IDEducationLevel", NUMBER(asdecimal=False)),
    Column("IDEducationSource", NUMBER(asdecimal=False)),
    Column("IDEducationForm", NUMBER(asdecimal=False)),
    Column("idocso", Integer),
    Column("AdmissionNumber", NUMBER(asdecimal=False)),
    Column("Comment", CHAR(1)),
    Column("fk_competition", NUMBER(asdecimal=False)),
)


t_vw_ss_competitivegrouppr_2021 = Table(
    "vw$ss_competitivegrouppr_2021",
    metadata,
    Column("UID", NUMBER(asdecimal=False)),
    Column("UIDCompetitiveGroup", NUMBER(asdecimal=False)),
    Column("UIDSubdivisionOrg", CHAR(1)),
    Column("UIDEducationProgram", NUMBER(asdecimal=False)),
    comment="CompetitiveGroupProgram",
)


t_vw_ss_distadmissionvolume_2021 = Table(
    "vw$ss_distadmissionvolume_2021",
    metadata,
    Column("UID", NUMBER(asdecimal=False)),
    Column("UIDAdmissionVolume", NUMBER(asdecimal=False)),
    Column("IDDirection", Integer, nullable=False),
    Column("IDLevelBudget", NUMBER(asdecimal=False)),
    Column("name", VARCHAR(1000)),
    Column("Budget_o", NUMBER(asdecimal=False)),
    Column("Budget_oz", NUMBER(asdecimal=False)),
    Column("Budget_z", NUMBER(asdecimal=False)),
    Column("Quota_o", NUMBER(asdecimal=False)),
    Column("Quota_oz", NUMBER(asdecimal=False)),
    Column("Quota_z", NUMBER(asdecimal=False)),
    Column("Paid_o", NUMBER(asdecimal=False)),
    Column("Paid_oz", NUMBER(asdecimal=False)),
    Column("Paid_z", NUMBER(asdecimal=False)),
    Column("Target_o", NUMBER(asdecimal=False)),
    Column("Target_oz", NUMBER(asdecimal=False)),
    Column("Target_z", NUMBER(asdecimal=False)),
)


t_vw_ss_educationprogram_2021 = Table(
    "vw$ss_educationprogram_2021",
    metadata,
    Column("UID", NUMBER(asdecimal=False)),
    Column("Name", VARCHAR(766)),
    Column("IDEducationForm", NUMBER(asdecimal=False)),
    Column("fk_competition", NUMBER(asdecimal=False), nullable=False),
    Column("idocso", Integer, nullable=False),
)


t_vw_ss_entrancetest_2021 = Table(
    "vw$ss_entrancetest_2021",
    metadata,
    Column("UID", NUMBER(asdecimal=False)),
    Column("UIDCompetitiveGroup", NUMBER(asdecimal=False)),
    Column("fk_competition", NUMBER(asdecimal=False)),
    Column("IDEntranceTestType", NUMBER(asdecimal=False)),
    Column("TestName", VARCHAR(768)),
    Column("IsEge", NUMBER(asdecimal=False)),
    Column("MinScore", NUMBER(asdecimal=False)),
    Column("Priority", NUMBER(asdecimal=False)),
    Column("IDSubject", Integer),
    Column("UIDReplaceEntranceTest", NUMBER(asdecimal=False)),
)


t_vw_ss_entrancetestbenefit_2021 = Table(
    "vw$ss_entrancetestbenefit_2021",
    metadata,
    Column("UIDEntranceTest", NUMBER(asdecimal=False)),
    Column("UID", NUMBER(asdecimal=False)),
    Column("IDBenefit", NUMBER(asdecimal=False)),
    Column("IDOlympicDiplomaType", NUMBER(asdecimal=False)),
    Column("OlympicClasses", VARCHAR(0)),
    Column("IDOlympicLevel", NUMBER(asdecimal=False)),
    Column("OlympicProfiles", Integer, nullable=False),
    Column("EgeMinValue", NUMBER(asdecimal=False)),
    Column("subject_name", VARCHAR(200)),
)


t_vw_ss_entrancetestloc_2021 = Table(
    "vw$ss_entrancetestloc_2021",
    metadata,
    Column("UID", NUMBER(asdecimal=False)),
    Column("UIDEntranceTest", NUMBER(asdecimal=False)),
    Column("TestDate", VARCHAR(24)),
    Column("TestLocation", CHAR(14)),
    Column("EntrantsCount", NUMBER(asdecimal=False)),
)


t_vw_ss_subdivisionorg_2021 = Table(
    "vw$ss_subdivisionorg_2021",
    metadata,
    Column("UID", NUMBER(asdecimal=False)),
    Column("Name", VARCHAR(256)),
)


t_vw_ss_termsadmission_2021_189 = Table(
    "vw$ss_termsadmission_2021_189",
    metadata,
    Column("UIDCampaign", NUMBER(asdecimal=False)),
    Column("UID", NUMBER(asdecimal=False)),
    Column("Name", CHAR(10)),
    Column("IDTermsLsf", NUMBER(asdecimal=False)),
    Column("IDStage", NUMBER(asdecimal=False)),
    Column("StartEvent", VARCHAR(26)),
    Column("EndEvent", VARCHAR(26)),
)
