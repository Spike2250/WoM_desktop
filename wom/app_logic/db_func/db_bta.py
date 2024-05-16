import os
import sqlite3
from pathlib import Path
import json
import ast
from wom.app_logic.db_func.json_recording_case import json_recording
from wom.settings.paths import DATABASE_BTA, CASES_BTA_PATH


DATABASE = DATABASE_BTA


def write_all_data_to_db_bta(d):
    write_all_data_to_bta_table(d)
    write_fullness_table_bta(d)


def write_dict_to_json(d):
    if 'созданные_документы' in d:
        d['созданные_документы'] = str(d['созданные_документы'])
    if 'дневники_табл' in d:
        d['дневники_табл'] = str(d['дневники_табл'])
    json_recording(d, 'BTA')
    print('    Словарь (d) успешно записан в JSON-файл. ')


'''============================================================================
                    Функции для работы с базой данных БТА
============================================================================'''


# подготовка стандартного кортежа данных для добавления в БД
def prepare_data_for_db_bta(d, new=False):
    if new:
        data = (d['unic_number'],
                d['status_act'],
                d['ФИО_пациента'],
                d['дата_поступления'],
                d['МКБ'],
                d['ФИО_врача'],
                d['тип_стационара'],
                d['дата_выписки'],
                d['нужда_в_ЛН'])
    else:
        data = (d['status_act'],
                d['ФИО_пациента'],
                d['дата_поступления'],
                d['МКБ'],
                d['ФИО_врача'],
                d['тип_стационара'],
                d['дата_выписки'],
                d['нужда_в_ЛН'],
                d['unic_number'])
    return data


# Функция создания основной базы данных для хранения
def create_data_base_bta():
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            CREATE TABLE
            IF NOT EXISTS
            medical_case (
                case_id GUID PRIMARY KEY,
                status BOOL NOT NULL,
                full_name TEXT NOT NULL,
                adm_date TEXT,
                mkb10_ds TEXT,
                doctor_name TEXT,
                type_hosp TEXT,
                dis_date TEXT,
                sicklist_check TEXT)''')
        con.commit()
        print("SQLite: создаем таблицу medical_case... ", end='')
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")


# Добавление данных в базу
def insert_into_db_bta(d):
    '''
    '''
    data_to_insert = prepare_data_for_db_bta(d, True)

    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            INSERT INTO medical_case (
                case_id,
                status,
                full_name,
                adm_date,
                mkb10_ds,
                doctor_name,
                type_hosp,
                dis_date,
                sicklist_check)
            VALUES (?, ?, ?, ?, ?,
                    ?, ?, ?, ?)
            ''', data_to_insert)
        con.commit()
        print("SQLite: данные успешно добавлены. ")
        cur.close()
        write_dict_to_json(d)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")


# чтение словаря по UIN
def read_d_from_db_bta(case_uin):
    '''
    '''
    json_dict_name = f'{case_uin}.json'
    file_path_d_json = Path(CASES_BTA_PATH, json_dict_name)
    # проверяем наличие такого файла в директории
    if os.path.exists(file_path_d_json):
        with open(file_path_d_json, 'r') as file:
            d = json.load(file)
        print('Словарь (d) успешно прочитан из JSON-файла. ')
        # делаем из строки множество
        if 'созданные_документы' in d:
            d['созданные_документы'] = ast.literal_eval(
                d['созданные_документы'])
        if 'дневники_табл' in d:
            d['дневники_табл'] = ast.literal_eval(
                d['дневники_табл'])
        # if 'd_sol' in d:
        #     d['d_sol'] = ast.literal_eval(d['d_sol'])

        return d
    else:
        return None


# Обновление записи в базе данных
def update_case_db_bta(d):
    '''
    '''
    data_to_update = prepare_data_for_db_bta(d)

    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            UPDATE medical_case
            SET status = ?,
                full_name = ?,
                adm_date = ?,
                mkb10_ds = ?,
                doctor_name = ?,
                type_hosp = ?,
                dis_date = ?,
                sicklist_check = ?
            WHERE case_id = ?
            ''', data_to_update)
        con.commit()
        print("SQLite: данные успешно обновлены. ")
        cur.close()
        write_dict_to_json(d)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")


# чтение всех активных (находящихся на госпитализации) пациентов
def read_db_active_cases_bta():
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        query = '''
            SELECT type_hosp,
                   adm_date,
                   full_name,
                   mkb10_ds,
                   doctor_name,
                   sicklist_check,
                   case_id,
                   dis_date
            FROM medical_case WHERE status = 1'''
        cur.execute(query)
        data = cur.fetchall()
        print('SQLite: чтение данных активных пациентов... Ok')
        cur.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")

    if data is None:
        return None
    else:
        # распаковываем данные
        upg_data = []
        for case in data:
            upg_data.append({
                "type_hosp": case[0],
                "adm_date": case[1],
                "full_name": case[2],
                "mkb10_ds": case[3],
                "doctor_name": case[4],
                "sicklist_check": case[5],
                "case_id": case[6],
                "dis_date": case[7]
            })
        return upg_data


# чтение всех архивных (выписанных) пациентов
def read_db_archive_cases_bta():
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        query = '''
            SELECT type_hosp,
                   adm_date,
                   dis_date,
                   full_name,
                   mkb10_ds,
                   doctor_name,
                   sicklist_check,
                   case_id
            FROM medical_case
            WHERE status = 0'''
        cur.execute(query)
        data = cur.fetchall()
        print('SQLite: чтение данных пациентов из архива... Ok')
        cur.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")

    if data is None:
        return None
    else:
        # распаковываем данные
        upg_data = []
        for case in data:
            upg_data.append({
                "type_hosp": case[0],
                "adm_date": case[1],
                "dis_date": case[2],
                "full_name": case[3],
                "mkb10_ds": case[4],
                "doctor_name": case[5],
                "sicklist_check": case[6],
                "case_id": case[7]
            })
        return upg_data


# запись всех данных словаря в БД
def write_all_data_to_bta_table(d):
    '''
    '''
    # проверяем есть ли строка в БД с таким уникальным номером
    if read_d_from_db_bta(d['unic_number']) is not None:
        update_case_db_bta(d)  # UPDATE запрос, если есть
    else:
        insert_into_db_bta(d)  # INSERT запрос, если нет


'''============================================================================
            Функции для работы с базой данных контроля наполненности БТА
============================================================================'''


# подготовка стандартного кортежа данных для добавления в БД
def prepare_data_for_fullness_db_bta(d, new=False):
    '''
    'ФИО_пациента'
    'Соматический_статус'
    'Неврологический_статус'
    'Основной_диагноз'
    'лечение_таблетки'
    's_domen_1'
    'лабораторные_данные'
    'инструментальные_данные'
    'консультации_данные'
    'Соматический_статус_выписка'
    'Неврологический_статус_вып'
    'Основной_диагноз_вып'
    's_domen_dis_1'
    'вид_выбытия'
    'рекомендации_выписка'
    '''
    if new:
        data = (d['unic_number'],
                d['check_line'])
    else:
        data = (d['check_line'],
                d['unic_number'])
    return data


# Функция создания базы данных наполненности
def create_fullness_db_bta():
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            CREATE TABLE
            IF NOT EXISTS
            fullness (
                case_id GUID PRIMARY KEY,
                fullness TEXT)''')
        con.commit()
        print("SQLite: создаем таблицу fullness... ", end='')
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")


# Добавление данных в базу
def insert_into_fullness_db_bta(d):
    '''
    '''
    data_to_insert = prepare_data_for_fullness_db_bta(d, True)

    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            INSERT INTO fullness (
                case_id,
                fullness)
            VALUES (?, ?)
            ''', data_to_insert)
        con.commit()
        print("SQLite: данные успешно добавлены в таблицу наполненности. ")
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")


# Обновление записи в базе данных
def update_fullness_db_bta(d):
    '''
    '''
    data_to_update = prepare_data_for_fullness_db_bta(d)

    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            UPDATE fullness
            SET fullness = ?
            WHERE case_id = ?
            ''', data_to_update)
        con.commit()
        print("SQLite: данные успешно обновлены в таблице наполненности. ")
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")


# чтение активных пациентов для списка на выписку
def read_fullness_db_bta(uin):
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            SELECT fullness
            FROM fullness
            WHERE case_id = ?''', (uin,))
        data = cur.fetchone()
        cur.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()

    if data is None:
        return None
    else:
        return data


def write_fullness_table_bta(d):
    if read_fullness_db_bta(d['unic_number']) is not None:
        update_fullness_db_bta(d)
    else:
        create_fullness_db_bta()
        insert_into_fullness_db_bta(d)
