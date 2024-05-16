import ast
import os
from docxtpl import DocxTemplate
from pathlib import Path
from wom.app_logic.service_func import create_short_name, convert_date
from wom.settings.paths import (
    CREATED_FILES_PATH_OMR_FDAY,
    CREATED_FILES_PATH_OMR_DAY,
    TEMPLATES_PATH_OMR,
    CREATED_FILES_PATH_BTA_FDAY,
    CREATED_FILES_PATH_BTA_DAY,
    TEMPLATES_PATH_BTA,
)
from wom.settings.dep_omr import organisation as ORGS_DATA


def list_created_docs(some_set):
    n = 0
    string = ''
    for value in some_set:
        n += 1
        string += f'{n} - {value};\n'
    return f"{string}  Всего:   {n}"


# установка пути к корневой папке
def path_main_folder_upg(d):
    path = ''
    if 'тип_стационара' in d:
        if d['тип_стационара'] in {'БТ - круглосуточный'}:
            path = CREATED_FILES_PATH_BTA_FDAY
        elif d['тип_стационара'] in {'БТ - дневной'}:
            path = CREATED_FILES_PATH_BTA_DAY
        elif d['тип_стационара'] in {'Круглосуточный стационар'}:
            path = CREATED_FILES_PATH_OMR_FDAY
        elif d['тип_стационара'] in {'Дневной стационар'}:
            path = CREATED_FILES_PATH_OMR_DAY

    return path


# установка пути к папке с шаблонами
def path_templates_upgrade(d):
    path = ''
    if 'тип_стационара' in d:
        if d['тип_стационара'] in {'БТ - круглосуточный', 'БТ - дневной'}:
            path = TEMPLATES_PATH_BTA
        else:
            path = TEMPLATES_PATH_OMR
    return path


# генерация пути к файлу по файловой системе
def generate_path_to_new_file(d):
    pt_short_name = create_short_name(d['ФИО_пациента'])

    adm_date = convert_date(d['дата_поступления'])
    year_happening = f'{adm_date.strftime("%Y")} год'
    month_happening = f'{adm_date.strftime("%m")} - {adm_date.strftime("%B")}'
    date_happening = d['дата_поступления']
    folder_happening = f'{pt_short_name}, пост.{date_happening}'
    folder_name = f'{year_happening}/{month_happening}/{folder_happening}'
    if (main_folder := path_main_folder_upg(d)) == '':
        path_new_file = f'UNKNOWN/{folder_name}'
    else:
        path_new_file = f'{main_folder}/{folder_name}'

    return path_new_file


def open_folder_with_files(d):
    os.startfile(Path(Path.cwd(), generate_path_to_new_file(d)))


def add_organisation_info(func):
    def inner(d, templates):
        merged_d = {**d, **ORGS_DATA}
        func(merged_d, templates)
    return inner


# создание документов
@add_organisation_info
def creating_documents(d, templates=None):
    if templates is None:
        templates = ['test']

    # перебираем список шаблонов и создаем документы
    for template in templates:
        key = 'созданные_документы'
        if key not in d:
            d[key] = set()
        else:
            if isinstance(d[key], str):
                d[key] = ast.literal_eval(d[key])
        # создание имени нового файла и пути для его сохранения
        docName = f"{create_short_name(d['ФИО_пациента'])}, {template}.docx"
        # создаем путь к новому файлу
        path_new_file = generate_path_to_new_file(d)
        # формируем окончательное имя файла
        filepath = Path(Path.cwd(), path_new_file, docName)

        # создаем документ на основе шаблона
        doc = DocxTemplate(Path(
            Path.cwd(),
            path_templates_upgrade(d),
            template + '.docx'))
        # создание файла по шаблону на основе словаря
        doc.render(d)
        # создаем папок на пути к файлу
        os.makedirs(path_new_file, exist_ok=True)
        # сохранение файла по указанному пути, с указанным именем
        doc.save(filepath)

        # добавляем название документа в список созданных
        d[key].add(template)
