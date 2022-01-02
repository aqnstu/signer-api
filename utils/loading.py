# -*- coding: utf-8 -*-
from minio import Minio
import io
<<<<<<< HEAD

from utils.signer import sign_file
=======
import os

from configs.minio import MINIO

client = Minio(
    f"{MINIO['host']}:{MINIO['port']}",
    access_key=MINIO["access_key"],
    secret_key=MINIO["secret_key"],
    secure=False,
)
>>>>>>> origin/master


def download(bucket: str, minio_id: str) -> str:
    """
    Скачиваем файл из minio
    :param bucket:
    :param minio_id:
<<<<<<< HEAD
    :return: путь с скачанному файлу
    """
    client = Minio('minio-node01.ciu.nstu.ru:9000',
                   access_key='9GKS1AQZY9aYFuHNxIDW',
                   secret_key='Aaj1u5SnjfyWlCXvgHVj',
                   secure=False)
    data = client.get_object(bucket, minio_id)
    file_name = minio_id.split('/')[1]
    with open(f'/home/api/signer-api/files/{file_name}', 'wb') as file_data:
=======

    :return: путь с скачанному файлу
    """
    data = client.get_object(bucket, minio_id)

    file_name = minio_id.split("/")[1]
    with open(os.path.join("files", "minio", file_name), "wb") as file_data:
>>>>>>> origin/master
        for d in data.stream(32 * 1024):
            file_data.write(d)
    return file_name


<<<<<<< HEAD
def upload(bucket: str, minio_id: str, file_name_sign: str) -> dict:
=======
def upload(bucket: str, minio_id: str, file_name_sign: str) -> str:
>>>>>>> origin/master
    """
    Загружаем в minio
    :param bucket:
    :param minio_id: исходный minio_id
    :param file_name_sign: путь к файлу подписи
<<<<<<< HEAD
    :return:
    """
    value_as_bytes = open(f'/home/api/signer-api/files/{file_name_sign}', 'rb').read()
    value_as_a_stream = io.BytesIO(value_as_bytes)
    src_catalog = minio_id.split('/')[0]
    new_mino_id = '/'.join([src_catalog, file_name_sign])
    try:
        client = Minio('minio-node01.ciu.nstu.ru:9000',
                       access_key='9GKS1AQZY9aYFuHNxIDW',
                       secret_key='Aaj1u5SnjfyWlCXvgHVj',
                       secure=False)
        try:
            client.put_object(bucket, new_mino_id, value_as_a_stream, len(value_as_bytes),
                              metadata={'Download_name': new_mino_id})
            return {'uploaded': new_mino_id}
        except Exception as err:
            return {'err': str(err)}
    except Exception as err:
        return {'err': str(err)}


if __name__ == '__main__':
    bucket = 'secdepresult'
    minio_id = '129/orlov_svedeniya_o_prieme.pdf'
    file_name = download(bucket, minio_id)
    print(file_name)
    file_name_sign = sign_file(file_name)
    print(file_name_sign)
    minio_id_sign = upload(bucket, minio_id, file_name_sign)
    print(minio_id_sign)
=======

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
>>>>>>> origin/master
