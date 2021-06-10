# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from configs.db import DB

SQLALCHEMY_DATABASE_URL = f"{DB['name']}+{DB['driver']}://{DB['username']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['section']}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
