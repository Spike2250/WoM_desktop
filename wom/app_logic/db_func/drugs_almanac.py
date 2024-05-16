import os
import json
from wom.settings.paths import ALMANAC_FILE


# чтение альманаха из json в словарь
def read_almanac():
    '''
    '''
    # проверяем наличие такого файла в директории
    if os.path.exists(ALMANAC_FILE):
        with open(ALMANAC_FILE, 'r') as file:
            d = json.load(file)
        return d
    else:
        return None


# запись альманаха в json
def almanac_json_recording(d):
    # записываем словарь в отдельный файл в формате json
    with open(ALMANAC_FILE, 'w') as file:
        json.dump(d, file, indent=4)
