# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, Integer, Table, Text, VARCHAR, text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


t_ss_admissionvolume = Table(
    "ss_admissionvolume",
    metadata,
    Column(
        "UID",
        NUMBER(asdecimal=True),
        comment="Уникальный идентификатор записи КЦП ООВО",
    ),
    Column(
        "UIDCampaign",
        NUMBER(asdecimal=True),
        comment="Уникальный идентификатор приемной кампании ООВО",
    ),
    Column(
        "IDDirection",
        Integer,
        comment="Идентификатор направления подготовки – содержит ссылку на id справочника Directions",
    ),
    Column(
        "IDEducationLevel",
        NUMBER(asdecimal=True),
        comment="Идентификатор уровня образования – содержит ссылку на id справочника educationLevel",
    ),
    Column("name", VARCHAR(1000), comment="Имя по ОКСО (не используется в выгрузке)"),
    Column(
        "Budget_o", NUMBER(asdecimal=True), comment="Значение в разрезе бюджет/очно"
    ),
    Column(
        "Budget_oz",
        NUMBER(asdecimal=True),
        comment="Значение в разрезе бюджет/очно-заочно",
    ),
    Column(
        "Budget_z", NUMBER(asdecimal=True), comment="Значение в разрезе бюджет/заочно"
    ),
    Column("Quota_o", NUMBER(asdecimal=True), comment="Значение в разрезе квота/очно"),
    Column(
        "Quota_oz",
        NUMBER(asdecimal=True),
        comment="Значение в разрезе квота/очно-заочно",
    ),
    Column(
        "Quota_z", NUMBER(asdecimal=True), comment="Значение в разрезе квота/заочно"
    ),
    Column("Paid_o", NUMBER(asdecimal=True), comment="Значение в разрезе платно/очно"),
    Column(
        "Paid_oz",
        NUMBER(asdecimal=True),
        comment="Значение в разрезе платно/очно-заочно",
    ),
    Column(
        "Paid_z", NUMBER(asdecimal=True), comment="Значение в разрезе платно/заочно"
    ),
    Column(
        "Target_o", NUMBER(asdecimal=True), comment="Значение в разрезе целевое/очно"
    ),
    Column(
        "Target_oz",
        NUMBER(asdecimal=True),
        comment="Значение в разрезе целевое/очно-заочно",
    ),
    Column(
        "Target_z", NUMBER(asdecimal=True), comment="Значение в разрезе целевое/заочно"
    ),
    comment="Контрольные цифры приема ",
)


class SsAppealstatus(Base):
    __tablename__ = "ss_appealstatuses"
    __table_args__ = {"comment": "Статус апелляции"}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(50))


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
    Column("UID", NUMBER(asdecimal=True)),
    Column("Name", VARCHAR(276)),
    Column("YearStart", NUMBER(asdecimal=True)),
    Column("YearEnd", NUMBER(asdecimal=True)),
    Column("IDEducationForm1", NUMBER(asdecimal=True)),
    Column("IDEducationForm2", NUMBER(asdecimal=True)),
    Column("IDEducationLevel1", NUMBER(asdecimal=True)),
    Column("IDEducationLevel2", NUMBER(asdecimal=True)),
    Column("IDCampaignType", NUMBER(asdecimal=True)),
    Column("IDCampaignStatus", NUMBER(asdecimal=True)),
    Column("NumberAgree", NUMBER(asdecimal=True)),
    Column("CountDirections", NUMBER(asdecimal=True)),
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
    Column("UID", NUMBER(asdecimal=True)),
    Column("UIDCampaign", NUMBER(asdecimal=True)),
    Column("Name", VARCHAR(786)),
    Column("IDLevelBudget", NUMBER(asdecimal=True)),
    Column("IDEducationLevel", NUMBER(asdecimal=True)),
    Column("IDEducationSource", NUMBER(asdecimal=True)),
    Column("IDEducationForm", NUMBER(asdecimal=True)),
    Column("idocso", Integer),
    Column("AdmissionNumber", NUMBER(asdecimal=True)),
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
    Column("uid_epgu", NUMBER(asdecimal=True)),
    Column("sogl", NUMBER(asdecimal=True)),
    Column("otzyv", NUMBER(asdecimal=True)),
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
    Column("sex", NUMBER(asdecimal=True)),
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
    Column("app_number", NUMBER(asdecimal=True)),
    Column("date_load", DateTime),
    Column("fk_abit_card", NUMBER(asdecimal=True)),
    Column("need_hostel", NUMBER(asdecimal=True)),
    Column("nh", VARCHAR(1000)),
)


t_ss_try = Table(
    "ss_try",
    metadata,
    Column("q", NUMBER(asdecimal=True)),
    Column("w", NUMBER(asdecimal=True)),
    Column("e", NUMBER(asdecimal=True)),
    Column("r", NUMBER(asdecimal=True)),
    Column("t", NUMBER(asdecimal=True)),
    Column("y", NUMBER(asdecimal=True)),
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
    Column("UID", NUMBER(asdecimal=True)),
    Column("UIDCampaign", NUMBER(asdecimal=True)),
    Column("IDDirection", Integer, nullable=False),
    Column("IDEducationLevel", NUMBER(asdecimal=True)),
    Column("name", VARCHAR(1000)),
    Column("Budget_o", NUMBER(asdecimal=True)),
    Column("Budget_oz", NUMBER(asdecimal=True)),
    Column("Budget_z", NUMBER(asdecimal=True)),
    Column("Quota_o", NUMBER(asdecimal=True)),
    Column("Quota_oz", NUMBER(asdecimal=True)),
    Column("Quota_z", NUMBER(asdecimal=True)),
    Column("Paid_o", NUMBER(asdecimal=True)),
    Column("Paid_oz", NUMBER(asdecimal=True)),
    Column("Paid_z", NUMBER(asdecimal=True)),
    Column("Target_o", NUMBER(asdecimal=True)),
    Column("Target_oz", NUMBER(asdecimal=True)),
    Column("Target_z", NUMBER(asdecimal=True)),
)


t_vw_ss_campaign_2021 = Table(
    "vw$ss_campaign_2021",
    metadata,
    Column("UID", NUMBER(asdecimal=True)),
    Column("Name", VARCHAR(276)),
    Column("YearStart", NUMBER(asdecimal=True)),
    Column("YearEnd", NUMBER(asdecimal=True)),
    Column("IDEducationForm1", NUMBER(asdecimal=True)),
    Column("IDEducationForm2", NUMBER(asdecimal=True)),
    Column("IDEducationLevel1", NUMBER(asdecimal=True)),
    Column("IDEducationLevel2", NUMBER(asdecimal=True)),
    Column("IDCampaignType", NUMBER(asdecimal=True)),
    Column("IDCampaignStatus", NUMBER(asdecimal=True)),
    Column("NumberAgree", NUMBER(asdecimal=True)),
    Column("CountDirections", NUMBER(asdecimal=True)),
    Column("EndDate", VARCHAR(26)),
)


t_vw_ss_competitivebenefit_2021 = Table(
    "vw$ss_competitivebenefit_2021",
    metadata,
    Column("UIDCompetitiveGroup", NUMBER(asdecimal=True)),
    Column("IDBenefit", NUMBER(asdecimal=True)),
    Column("IDOlympicDiplomaType", NUMBER(asdecimal=True)),
    Column("EgeMinValue", NUMBER(asdecimal=True)),
    Column("IDOlympicType", NUMBER(asdecimal=True)),
    Column("IDOlympicLevels", NUMBER(asdecimal=True)),
    Column("OlympicProfiles", VARCHAR(0)),
    Column("UID", NUMBER(asdecimal=True)),
    Column("fk_competition", NUMBER(asdecimal=True)),
)


t_vw_ss_competitivegroup_2021 = Table(
    "vw$ss_competitivegroup_2021",
    metadata,
    Column("UID", NUMBER(asdecimal=True)),
    Column("UIDCampaign", NUMBER(asdecimal=True)),
    Column("Name", VARCHAR(801)),
    Column("IDLevelBudget", NUMBER(asdecimal=True)),
    Column("IDEducationLevel", NUMBER(asdecimal=True)),
    Column("IDEducationSource", NUMBER(asdecimal=True)),
    Column("IDEducationForm", NUMBER(asdecimal=True)),
    Column("idocso", Integer),
    Column("AdmissionNumber", NUMBER(asdecimal=True)),
    Column("Comment", CHAR(1)),
    Column("fk_competition", NUMBER(asdecimal=True)),
)


t_vw_ss_competitivegrouppr_2021 = Table(
    "vw$ss_competitivegrouppr_2021",
    metadata,
    Column("UID", NUMBER(asdecimal=True)),
    Column("UIDCompetitiveGroup", NUMBER(asdecimal=True)),
    Column("UIDSubdivisionOrg", CHAR(1)),
    Column("UIDEducationProgram", NUMBER(asdecimal=True)),
    comment="CompetitiveGroupProgram",
)


t_vw_ss_distadmissionvolume_2021 = Table(
    "vw$ss_distadmissionvolume_2021",
    metadata,
    Column("UID", NUMBER(asdecimal=True)),
    Column("UIDAdmissionVolume", NUMBER(asdecimal=True)),
    Column("IDDirection", Integer, nullable=False),
    Column("IDLevelBudget", NUMBER(asdecimal=True)),
    Column("name", VARCHAR(1000)),
    Column("Budget_o", NUMBER(asdecimal=True)),
    Column("Budget_oz", NUMBER(asdecimal=True)),
    Column("Budget_z", NUMBER(asdecimal=True)),
    Column("Quota_o", NUMBER(asdecimal=True)),
    Column("Quota_oz", NUMBER(asdecimal=True)),
    Column("Quota_z", NUMBER(asdecimal=True)),
    Column("Paid_o", NUMBER(asdecimal=True)),
    Column("Paid_oz", NUMBER(asdecimal=True)),
    Column("Paid_z", NUMBER(asdecimal=True)),
    Column("Target_o", NUMBER(asdecimal=True)),
    Column("Target_oz", NUMBER(asdecimal=True)),
    Column("Target_z", NUMBER(asdecimal=True)),
)


t_vw_ss_educationprogram_2021 = Table(
    "vw$ss_educationprogram_2021",
    metadata,
    Column("UID", NUMBER(asdecimal=True)),
    Column("Name", VARCHAR(766)),
    Column("IDEducationForm", NUMBER(asdecimal=True)),
    Column("fk_competition", NUMBER(asdecimal=True), nullable=False),
    Column("idocso", Integer, nullable=False),
)


t_vw_ss_entrancetest_2021 = Table(
    "vw$ss_entrancetest_2021",
    metadata,
    Column("UID", NUMBER(asdecimal=True)),
    Column("UIDCompetitiveGroup", NUMBER(asdecimal=True)),
    Column("fk_competition", NUMBER(asdecimal=True)),
    Column("IDEntranceTestType", NUMBER(asdecimal=True)),
    Column("TestName", VARCHAR(768)),
    Column("IsEge", NUMBER(asdecimal=True)),
    Column("MinScore", NUMBER(asdecimal=True)),
    Column("Priority", NUMBER(asdecimal=True)),
    Column("IDSubject", Integer),
    Column("UIDReplaceEntranceTest", NUMBER(asdecimal=True)),
)


t_vw_ss_entrancetestbenefit_2021 = Table(
    "vw$ss_entrancetestbenefit_2021",
    metadata,
    Column("UIDEntranceTest", NUMBER(asdecimal=True)),
    Column("UID", NUMBER(asdecimal=True)),
    Column("IDBenefit", NUMBER(asdecimal=True)),
    Column("IDOlympicDiplomaType", NUMBER(asdecimal=True)),
    Column("OlympicClasses", VARCHAR(0)),
    Column("IDOlympicLevel", NUMBER(asdecimal=True)),
    Column("OlympicProfiles", Integer, nullable=True),
    Column("EgeMinValue", NUMBER(asdecimal=True)),
    Column("subject_name", VARCHAR(200)),
)


t_vw_ss_entrancetestloc_2021 = Table(
    "vw$ss_entrancetestloc_2021",
    metadata,
    Column("UID", NUMBER(asdecimal=True)),
    Column("UIDEntranceTest", NUMBER(asdecimal=True)),
    Column("TestDate", VARCHAR(24)),
    Column("TestLocation", CHAR(14)),
    Column("EntrantsCount", NUMBER(asdecimal=True)),
)


t_vw_ss_subdivisionorg_2021 = Table(
    "vw$ss_subdivisionorg_2021",
    metadata,
    Column("UID", NUMBER(asdecimal=True)),
    Column("Name", VARCHAR(256)),
)


t_vw_ss_termsadmission_2021_189 = Table(
    "vw$ss_termsadmission_2021_189",
    metadata,
    Column("UIDCampaign", NUMBER(asdecimal=True)),
    Column("UID", NUMBER(asdecimal=True)),
    Column("Name", CHAR(10)),
    Column("IDTermsLsf", NUMBER(asdecimal=True)),
    Column("IDStage", NUMBER(asdecimal=True)),
    Column("StartEvent", VARCHAR(26)),
    Column("EndEvent", VARCHAR(26)),
)


t_ss_termsadmission = Table(
    'ss_termsadmission', metadata,
    Column('UIDCampaign', NUMBER(asdecimal=True)),
    Column('UID', NUMBER(asdecimal=True)),
    Column('Name', VARCHAR(500)),
    Column('IDTermsLfs', NUMBER(asdecimal=True)),
    Column('IDStage', NUMBER(asdecimal=True)),
    Column('StartEvent', VARCHAR(26)),
    Column('EndEvent', VARCHAR(26))
)


class SsApplicationstatus(Base):
    __tablename__ = 'ss_applicationstatuses'
    __table_args__ = {'schema': 'abituser', 'comment': 'Статусы заявлений'}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    code = Column(VARCHAR(100))
    name = Column(VARCHAR(200))


class SsEntityType(Base):
    __tablename__ = 'ss_entity_type'
    __table_args__ = {'schema': 'abituser'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    name = Column(VARCHAR(512), nullable=False)


class SsEpguapplication(Base):
    __tablename__ = 'ss_epguapplication'
    __table_args__ = {'schema': 'abituser'}

    pk = Column(NUMBER(asdecimal=False), primary_key=True)
    epgu_id = Column(VARCHAR(128))
    json = Column(Text)
    date_add = Column(DateTime, nullable=False, server_default=text("sysdate "))
    is_accepted = Column(NUMBER(asdecimal=False), nullable=False, server_default=text("0 "))
    date_accept = Column(DateTime)
    remark = Column(VARCHAR(4000))
    id_ss_entity_type = Column(ForeignKey('abituser.ss_entity_type.id'), nullable=False)
    epgu_application_id = Column(Integer)
    id_jwt = Column(NUMBER(asdecimal=True))

    ss_entity_type = relationship('SsEntityType')


class SsStatusesTo(Base):
    __tablename__ = 'ss_statuses_to'
    __table_args__ = {'schema': 'abituser'}

    pk = Column(NUMBER(asdecimal=True), primary_key=True)
    epgu_id = Column(VARCHAR(128), nullable=False, comment='id на ЕПГУ')
    id_ss_applicationstatuses = Column(ForeignKey('abituser.ss_applicationstatuses.id'), nullable=False, comment='статус')
    date_add = Column(DateTime, nullable=False, server_default=text("sysdate "), comment='дата добавления в очередь')
    is_processed = Column(NUMBER(asdecimal=True), nullable=False, server_default=text("0 "), comment='обработан ли, при ошибке -1')
    date_process = Column(DateTime, comment='дата обработки')
    err_msg = Column(VARCHAR(4000), comment='сообщение об ошибке')
    epgu_application_id = Column(Integer)
    remark = Column(VARCHAR(500))

    ss_applicationstatus = relationship('SsApplicationstatus')


class SsDocumenttype(Base):
    __tablename__ = 'ss_documenttypes'
    __table_args__ = {'schema': 'abituser', 'comment': 'Типы документов'}

    id = Column(Integer, primary_key=True)
    actual = Column(Integer)
    name = Column(VARCHAR(1000))
    idcategory = Column(Integer)
    idsyscategory = Column(Integer)


class SsEpgudocument(Base):
    __tablename__ = 'ss_epgudocument'
    __table_args__ = {'schema': 'abituser'}

    pk = Column(Integer, primary_key=True)
    epgu_id = Column(VARCHAR(128), nullable=False)
    json = Column(Text)
    date_add = Column(DateTime, nullable=False, server_default=text("sysdate "))
    is_accepted = Column(NUMBER(asdecimal=False), nullable=False, server_default=text("0 "))
    date_accept = Column(DateTime)
    remark = Column(VARCHAR(4000))
    id_ss_documenttype = Column(ForeignKey('abituser.ss_documenttypes.id'), nullable=False)
    epgu_application_id = Column(Integer)
    id_jwt = Column(Integer)

    ss_documenttype = relationship('SsDocumenttype')

class SsAchievementcategory(Base):
    __tablename__ = 'ss_achievementcategories'
    __table_args__ = {'schema': 'abituser', 'comment': 'Категории индивидуальных достижений'}

    id = Column(Integer, primary_key=True)
    Actual = Column(Integer)
    Name = Column(VARCHAR(500))


class SsEpguachievement(Base):
    __tablename__ = 'ss_epguachievement'
    __table_args__ = {'schema': 'abituser'}

    pk = Column(NUMBER(asdecimal=False), primary_key=True)
    epgu_id = Column(VARCHAR(128), nullable=False)
    json = Column(Text)
    date_add = Column(DateTime, nullable=False, server_default=text("sysdate "))
    is_accepted = Column(NUMBER(asdecimal=False), nullable=False, server_default=text("0       "))
    date_accept = Column(DateTime)
    remark = Column(VARCHAR(4000))
    id_ss_category = Column(ForeignKey('abituser.ss_achievementcategories.id'), nullable=False)
    epgu_application_id = Column(NUMBER(asdecimal=False))
    id_jwt = Column(Integer)

    ss_achievementcategory = relationship('SsAchievementcategory')
