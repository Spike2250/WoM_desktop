from pathlib import Path
import json

from wom.settings.paths import CASES_PATH


# запись словаря в json
def json_recording(d, type_=None):
    # записываем словарь в отдельный файл в формате json

    json_dict_name = f'{d["unic_number"]}.json'
    folder_path = CASES_PATH if type_ is None else f'{CASES_PATH}/{type_}'
    json_file_path = Path(Path.cwd(), folder_path, json_dict_name)
    with open(json_file_path, 'w') as file:
        json.dump(d, file, indent=2)
