import boto3
from botocore.exceptions import ClientError
# from wom.app_logic.db_func.db_omr import DATABASE
import os as oper_system
from dotenv import load_dotenv


load_dotenv()


BUCKET_MAIN = 'omrdbjson'
AWS_ACCESS_KEY_ID = oper_system.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = oper_system.getenv('AWS_SECRET_ACCESS_KEY')


# Yandex Object Storage Access
os = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name='ru-central1',
    endpoint_url='https://storage.yandexcloud.net'
)


"""====================================================
Базовые функции
===================================================="""


# Перечень корзин
def print_list_buckets():
    for bucket in os.list_buckets()['Buckets']:
        print(bucket['Name'])


# Перечень объектов в бакете
def print_keys_from_bucket(bucket_name):
    for key in os.list_objects(Bucket=bucket_name)['Contents']:
        print(key['Key'])


# Создание бакета
def make_bucket(bucket_name):
    os.create_bucket(Bucket=bucket_name)


# Удалить объект из бакета
def delete_from_bucket(bucket_name, object_name):
    os.delete_object(Bucket=bucket_name, Key=object_name)


"""====================================================
Для историй болезни json
===================================================="""


# Запись объекта в бакет
def upload_case_to_bucket(bucket_name, object_name, folder):
    os.upload_file(f"AWP_WoM/wom/JSON/{folder}/{object_name}",
                   bucket_name, object_name)
    print(f'{object_name} успешно загружен в bucket YandexCloud')


# Загрузить объект из бакета
def download_case_from_bucket(bucket_name, object_name, folder):
    os.download_file(bucket_name, object_name,
                     f"AWP_WoM/wom/JSON/{folder}/{object_name}")
    print(f'{object_name} успешно скачан из bucket YandexCloud')


def download_case_from_yandex_cloud_bucket(type_):
    def wrapper(read_d):
        def inner(*args, **kwargs):
            download_case_from_bucket(bucket_name=BUCKET_MAIN,
                                      folder=type_.upper(),
                                      object_name=f'{args[1]}.json')
            read_d(*args, **kwargs)
        return inner
    return wrapper


def upload_history_to_yandex_cloud_bucket(type_):
    def wrapper(save_history):
        def inner(d):
            DATABASE = define_database(type_)
            # скачиваем актуальную БД из бакета
            # (для минимизации возможного расхождения с уже скачаной)
            download_db_from_bucket(bucket_name=BUCKET_MAIN,
                                    db_name=DATABASE)
            # сохраняем данные
            save_history(d)
            # загружаем в бакет
            upload_db_to_bucket(bucket_name=BUCKET_MAIN,
                                db_name=DATABASE)
            upload_case_to_bucket(bucket_name=BUCKET_MAIN,
                                  folder=type_.upper(),
                                  object_name=f"{d['unic_number']}.json")
        return inner
    return wrapper


"""====================================================
Для базы данных
===================================================="""


# Запись БД в бакет
def upload_db_to_bucket(bucket_name, db_name):
    os.upload_file(f"AWP_WoM/databases/{db_name}", bucket_name, db_name)
    print(f'База данных {db_name} успешно загружена в bucket YandexCloud')


# Загрузить БД из бакета
def download_db_from_bucket(bucket_name, db_name):
    os.download_file(bucket_name, db_name, f"AWP_WoM/databases/{db_name}")
    print(f'База данных {db_name} успешно скачана из bucket YandexCloud')


def define_database(type_):
    if type_ == 'omr':
        from wom.app_logic.db_func.db_omr import DATABASE as omr
        database = omr.split('/')[1]
    elif type_ == 'bta':
        from wom.app_logic.db_func.db_bta import DATABASE as bta
        database = bta.split('/')[1]
    return database


def download_db_from_yandex_cloud_bucket(type_):
    def wrapper(func):
        def inner(*args, **kwargs):
            DATABASE = define_database(type_)
            download_db_from_bucket(bucket_name=BUCKET_MAIN,
                                    db_name=DATABASE)
            func(*args, **kwargs)
        return inner
    return wrapper


"""====================================================
Для шаблонов в БД
===================================================="""


def define_database_templates(type_):
    if type_ == 'default_templates':
        from wom.app_logic.db_func.db_st_obj_templates import DATABASE as db
        database = db.split('/')[1]
    return database


def download_templates_db_from_yandex_cloud_bucket(type_):
    def wrapper(func):
        def inner(*args, **kwargs):
            DATABASE = define_database_templates(type_)
            download_db_from_bucket(bucket_name=BUCKET_MAIN,
                                    db_name=DATABASE)
            func(*args, **kwargs)
        return inner
    return wrapper


def upload_templates_db_from_yandex_cloud_bucket(type_):
    def wrapper(func):
        def inner(*args, **kwargs):
            func(*args, **kwargs)
            DATABASE = define_database_templates(type_)
            upload_db_to_bucket(bucket_name=BUCKET_MAIN,
                                db_name=DATABASE)
        return inner
    return wrapper


"""====================================================
Для шаблонов json
===================================================="""


# Запись шаблонов в бакет
def upload_templates_to_bucket(bucket_name, templates_name):
    os.upload_file(f"wom/Almanac/{templates_name}.json",
                   bucket_name,
                   f"templates/{templates_name}.json")
    print(f'Шаблоны {templates_name} успешно загружены в bucket YandexCloud')


# Загрузить шаблоны из бакета
def download_templates_from_bucket(bucket_name, templates_name):
    try:
        os.download_file(bucket_name,
                         f"templates/{templates_name}.json",
                         f"wom/Almanac/{templates_name}.json")
        msg = f'Шаблоны {templates_name} успешно '\
              f'скачаны из bucket YandexCloud'
        print(msg)
    # file not found
    except ClientError:
        pass


def download_templates_json_from_yandex_cloud_bucket(templates_name):
    def wrapper(func):
        def inner(*args, **kwargs):
            download_templates_from_bucket(bucket_name=BUCKET_MAIN,
                                           templates_name=templates_name)
            func(*args, **kwargs)
        return inner
    return wrapper


def upload_templates_json_from_yandex_cloud_bucket(templates_name):
    upload_templates_to_bucket(bucket_name=BUCKET_MAIN,
                               templates_name=templates_name)


# отдельная функция для ICF шаблонов (ввиду непонимая как использовать,
# декоратор с параметром в виде атрибута класса)
def download_templates_icf_json_from_yandex_cloud_bucket(templates_name):
    download_templates_from_bucket(bucket_name=BUCKET_MAIN,
                                   templates_name=templates_name)
