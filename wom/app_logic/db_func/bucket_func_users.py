from wom.app_logic.db_func.bucket_func import os


BUCKET = 'users'


# Создание бакета
def make_bucket():
    os.create_bucket(Bucket=BUCKET)


def upload_user_info_from_yandex_cloud_bucket(user_id):
    pass


def download_user_info_from_yandex_cloud_bucket(user_id):
    pass
