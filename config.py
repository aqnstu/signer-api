# -*- coding: utf-8 -*-
TEST = {
    "BASE_URL": "http://85.142.162.12:8031",
    "OGRN": "1025401485010",
    "KPP": "540401001",
}

PROD = {
    "BASE_URL": "http://10.3.60.3:8031",
    "OGRN": "1025401485010",
    "KPP": "540401001",
}

LOG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "ss-logger": {"handlers": ["default"], "level": "DEBUG"},
    },
}
