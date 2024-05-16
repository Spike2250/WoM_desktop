from pathlib import Path


_main_path = 'wom'
_cases_omr = 'OMR'
_cases_bta = 'BTA'

ALMANAC_PATH = f'{_main_path}/Almanac'
_almanac_file = 'Almanac.json'
ALMANAC_FILE = Path(Path.cwd(), ALMANAC_PATH, _almanac_file)

_databases_path = f'{_main_path}/databases'
_db_omr = 'omr_database.db'
_db_bta = 'bta_database.db'
_db_templates = 'templates.db'
DATABASE_OMR = Path(Path.cwd(), _databases_path, _db_omr)
DATABASE_BTA = Path(Path.cwd(), _databases_path, _db_bta)
DATABASE_TEMPLATES = Path(Path.cwd(), _databases_path, _db_templates)

CASES_PATH = f'{_databases_path}/cases_JSON'
CASES_OMR_PATH = Path(Path.cwd(), CASES_PATH, _cases_omr)
CASES_BTA_PATH = Path(Path.cwd(), CASES_PATH, _cases_bta)


CREATED_FILES_PATH = f'{_main_path}/БАЗА ДАННЫХ ДОКУМЕНТОВ'
FULLDAY_REGIMEN = 'Круглосуточный стационар'
DAY_REGIMEN = 'Дневной стационар'
TEMPLATES_FOLDER = 'templates'
TEMPLATES_PATH_OMR = f'{_main_path}/{TEMPLATES_FOLDER}/{_cases_omr}'
TEMPLATES_PATH_BTA = f'{_main_path}/{TEMPLATES_FOLDER}/{_cases_bta}'

PATIENT_LISTS_PATH = f'{CREATED_FILES_PATH}/Списки пациентов'

OMR_NAME = 'Отделение медицинской реабилитации'
CREATED_FILES_PATH_OMR = f'{CREATED_FILES_PATH}/{OMR_NAME}'
CREATED_FILES_PATH_OMR_FDAY = f'{CREATED_FILES_PATH_OMR}/{FULLDAY_REGIMEN}'
CREATED_FILES_PATH_OMR_DAY = f'{CREATED_FILES_PATH_OMR}/{DAY_REGIMEN}'

BTA_NAME = 'Кабинет ботулинотерапии'
CREATED_FILES_PATH_BTA = f'{CREATED_FILES_PATH}/{BTA_NAME}'
CREATED_FILES_PATH_BTA_FDAY = f'{CREATED_FILES_PATH_BTA}/{FULLDAY_REGIMEN}'
CREATED_FILES_PATH_BTA_DAY = f'{CREATED_FILES_PATH_BTA}/{DAY_REGIMEN}'
