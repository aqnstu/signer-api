# -*- coding: utf-8 -*-
import base64
import os


def to_base64_string(s: str) -> str:
    """
    Конвертировать строку в стоку BASE64.
    """
    return base64.b64encode(s.encode("utf-8")).decode("utf-8")


def get_signature():
    """
    Получить подпись файла "file" с Header и Payload.
    """
    if os.path.isfile(os.path.join("files", "file")):
        os.system(
            "/opt/cprocsp/bin/amd64/cryptcp -sign -dn E=buhgalter@adm.nstu.ru "
            + "-hashAlg 1.2.643.7.1.1.2.2 -detached "
            + "/home/api/signer-api/files/file /home/api/signer-api/files/signature >/dev/null 2>&1"
        )
        with open(os.path.join("files", "signature"), "r") as f:
            signature = "".join(f.read().splitlines())
    else:
        raise Exception("NoFileForSignature")
    return signature


def sign_file(file_name: str) -> str:
    """
    Получить подпись файла в file_name.sgn
    :str file_name: имя файла
    :
    """
    new_name = '.'.join(file_name.split('.')[:-1])
    if os.path.isfile(os.path.join("files/minio", file_name)):
        os.system(
            "/opt/cprocsp/bin/amd64/cryptcp -sign -dn E=buhgalter@adm.nstu.ru "
            + "-hashAlg 1.2.643.7.1.1.2.2 -detached "
            + f"/home/api/signer-api/files/minio/{file_name} /home/api/signer-api/files/minio/{new_name}.sgn >/home/api/signer-api/files/sign.log 2>&1"
        )
        return f"{new_name}.sgn"
    else:
        raise Exception("NoFileForSignature")


def get_jwt(header: str, payload: str = None) -> str:
    """
    Получить JWT для запроса к API сервиса приема ССПВО.
    """
    header_base64 = to_base64_string(header)
    if payload:
        payload_base64 = to_base64_string(payload)
        to_signature = f"{header_base64}.{payload_base64}"
    else:
        to_signature = f"{header_base64}."
    with open(os.path.join("files", "file"), "w+") as f:
        f.write(to_signature)
    signature = get_signature()

    return f"{to_signature}.{signature}"
