import os
import json
from pathlib import Path
from wom.settings.paths import ALMANAC_PATH


def read_templates(templates_name):
    '''
    '''
    json_dict_name = f'{templates_name}.json'
    file_path_d_json = Path(Path.cwd(), ALMANAC_PATH, json_dict_name)
    # проверяем наличие такого файла в директории
    if os.path.exists(file_path_d_json):
        with open(file_path_d_json, 'r') as file:
            templates = json.load(file)
        return templates
    else:
        return None


def templates_json_recording(templates, templates_name):
    json_dict_name = f'{templates_name}.json'
    json_file_path = Path(Path.cwd(), ALMANAC_PATH, json_dict_name)
    with open(json_file_path, 'w') as file:
        json.dump(templates, file, indent=4)
