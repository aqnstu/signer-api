# -*- coding: utf-8 -*-

"""
Работа с внешним сервисом для отправки СМС (my3.webcom.mobi).
"""
import json
import requests as r
from typing import Union

from configs.sms import sms_config, URL_BALANCE, URL_SEND, URL_STATE


def get_balance() -> Union[str, None]:
    """
    Получить баланс.
    """
    body = {"login": sms_config.get("login"), "password": sms_config.get("password")}

    try:
        resp = r.post(
            URL_BALANCE,
            data=json.dumps(body),
            headers={
                "Content-Type": "application/json; charset=utf-8",
            },
        )
        money = resp.json().get("money")
    except Exception as e:
        money = str(e)

    return money if money else "Unknown error"


def get_number_available() -> list:
    """
    Получить количество доступных СМС для отправки.
    """
    body = {"login": sms_config.get("login"), "password": sms_config.get("password")}

    try:
        resp = r.post(
            URL_BALANCE,
            data=json.dumps(body).encode("utf8"),
            headers={
                "Content-Type": "application/json; charset=utf-8",
            },
        )
        information = resp.json().get("information")
    except Exception:
        information = []

    return information


def send_sms(phone: str, text: str) -> dict:
    """
    Отправить сообщение адресату ("GET" API).
    """
    params = {
        "user": sms_config.get("login"),
        "pwd": sms_config.get("password"),
        "sadr": sms_config.get("sender"),
        "text": text,
        "dadr": phone,
        "translite": 0,
    }

    try:
        resp = r.get(URL_SEND, params=params)
        ans = resp.text

    except Exception as e:
        return {"is_error": True, "id_sms": 0, "msg": str(e)}

    try:
        ans_int = int(ans)
    except ValueError:
        return {"is_error": True, "id_sms": 0, "msg": ans}

    return {"is_error": False, "id_sms": ans_int, "msg": ""}


def get_sms_state(id_sms: int) -> dict:
    """
    Получить статус SMS.
    """
    states = {
        "send": 1,
        "deliver": 2,  # конечный
        "partly_deliver": 3,  # в ТП
        "not_deliver": 4,  # конечный
        "expired": 5,  # конечный
    }

    params = {
        "user": sms_config.get("login"),
        "pwd": sms_config.get("password"),
        "smsid": id_sms,
    }

    try:
        resp = r.get(URL_STATE, params=params)
        ans = resp.text
    except Exception as e:
        return {"is_error": True, "status": "", "msg": str(e)}

    if ans not in states.keys():
        return {"is_error": True, "status": "", "msg": ans if ans else "Unknown error"}

    return {"is_error": False, "status": ans, "msg": ""}
