# -*- coding: utf-8 -*-
from minio import Minio
import io
import os

from configs.minio import MINIO

client = Minio(
    f"{MINIO['host']}:{MINIO['port']}",
    access_key=MINIO["access_key"],
    secret_key=MINIO["secret_key"],
    secure=False,
)


def download(bucket: str, minio_id: str) -> str:
    """
    Скачиваем файл из minio
    :param bucket:
    :param minio_id:

    :return: путь с скачанному файлу
    """
    data = client.get_object(bucket, minio_id)

    file_name = minio_id.split("/")[1]
    with open(os.path.join("files", "minio", file_name), "wb") as file_data:
        for d in data.stream(32 * 1024):
            file_data.write(d)
    return file_name


def upload(bucket: str, minio_id: str, file_name_sign: str) -> str:
    """
    Загружаем в minio
    :param bucket:
    :param minio_id: исходный minio_id
    :param file_name_sign: путь к файлу подписи

    :return:
    """
    value_as_bytes = open(os.path.join("files", "minio", file_name_sign), "rb").read()
    value_as_a_stream = io.BytesIO(value_as_bytes)
    src_catalog = minio_id.split("/")[0]

    new_mino_id = "/".join([src_catalog, file_name_sign])
    try:
        client.put_object(
            bucket,
            new_mino_id,
            value_as_a_stream,
            len(value_as_bytes),
            metadata={"Download_name": new_mino_id},
        )
        return {"uploaded": new_mino_id}
    except Exception as e:
        return {"error": str(e)}
