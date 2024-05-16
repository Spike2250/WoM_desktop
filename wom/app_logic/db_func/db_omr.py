import os
import sqlite3
from pathlib import Path
import json
import ast
from wom.app_logic.db_func.json_recording_case import json_recording
from wom.settings.paths import DATABASE_OMR, CASES_OMR_PATH


DATABASE = DATABASE_OMR


# запись всех данных словаря в БД
def write_all_data_to_db_omr(d):
    write_omr_table(d)
    write_fullness_table(d)
    write_scale_table(d)


def write_dict_to_json(d):
    if 'созданные_документы' in d:
        d['созданные_документы'] = str(d['созданные_документы'])
    if 'дневники_табл' in d:
        d['дневники_табл'] = str(d['дневники_табл'])
    json_recording(d, 'OMR')
    print('    Словарь (d) успешно записан в JSON-файл. ')


'''============================================================================
                    Функции для работы с основной базой данных
============================================================================'''


# подготовка стандартного кортежа данных для добавления в БД
def prepare_data_for_db(d, new=False):

    def _for_keys(data: list, keys: list, nutricia=False):
        if nutricia:
            for key in keys:
                data.append(d[key])
        else:
            for key in keys:
                if key != 'стол':
                    data.append(d[key])
                else:
                    data.append('')
        return data

    keys = [
        'status_act',
        'ФИО_пациента',
        'дата_поступления',
        'МКБ',
        'ФИО_врача',
        'тип_стационара',
        'дата_выписки',
        'стол',
        'нужда_в_ЛН',
        'палата']

    if new:
        data = [d['unic_number']]
        data = _for_keys(data, keys)
    else:
        if 'стол' in d:
            data = _for_keys([], keys, nutricia=True)
            data.append(d['unic_number'])
        else:
            data = _for_keys([], keys)
            data.append(d['unic_number'])

    return tuple(data)


# Функция создания основной базы данных для хранения
def create_data_base():
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
                diet TEXT,
                sicklist_check TEXT,
                room_number TEXT)''')
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
def insert_into_db(d):
    '''
    '''
    data_to_insert = prepare_data_for_db(d, True)

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
                diet,
                sicklist_check,
                room_number)
            VALUES (?, ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?)
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
def read_d_from_db(case_uin):
    '''
    '''
    # try:
    #     con = sqlite3.connect(DATABASE)
    #     cur = con.cursor()
    #     print("Подключен к SQLite")

    #     query = 'SELECT * FROM medical_case WHERE case_id = ?'
    #     cur.execute(query, [case_uin])
    #     data = cur.fetchone()
    #     print('SQLite: чтение данных... Ok')
    #     cur.close()

    # except sqlite3.Error as error:
    #     print("Ошибка при работе с SQLite", error)
    # finally:
    #     if con:
    #         con.close()
    #         print("    Соединение с SQLite успешно закрыто.")

    # if data is None:
    #     return None
    # else:
    #     return ast.literal_eval(data[-1])
    json_dict_name = f'{case_uin}.json'
    file_path_d_json = Path(CASES_OMR_PATH, json_dict_name)
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
def update_case_db(d):
    '''
    '''
    data_to_update = prepare_data_for_db(d)

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
                diet = ?,
                sicklist_check = ?,
                room_number = ?
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
def read_db_active_cases():
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        query = '''
            SELECT type_hosp,
                   adm_date,
                   room_number,
                   full_name,
                   mkb10_ds,
                   doctor_name,
                   sicklist_check,
                   diet,
                   case_id,
                   dis_date
            FROM medical_case WHERE status = 1'''
        cur.execute(query)
        data = cur.fetchall()
        print('SQLite: чтение данных активных пациентов... Ok')
        cur.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        if 'no such table' in error.__str__():
            create_data_base()
            read_db_active_cases()
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
                "room_number": case[2],
                "full_name": case[3],
                "mkb10_ds": case[4],
                "doctor_name": case[5],
                "sicklist_check": case[6],
                "diet": case[7],
                "case_id": case[8],
                "dis_date": case[9],
            })
        return upg_data


# чтение активных пациентов для списка на выписку
def read_db_active_cases_for_discharge():
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        query = '''
            SELECT type_hosp,
                   adm_date,
                   dis_date,
                   room_number,
                   full_name,
                   doctor_name,
                   sicklist_check,
                   case_id
            FROM medical_case
            WHERE status = 1'''
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
                "dis_date": case[2],
                "room_number": case[3],
                "full_name": case[4],
                "doctor_name": case[5],
                "sicklist_check": case[6],
                "case_id": case[7],
            })
        return upg_data


# чтение всех архивных (выписанных) пациентов
def read_db_archive_cases():
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
                "case_id": case[7],
            })
        return upg_data


# запись всех данных словаря в БД
def write_omr_table(d):
    '''
    '''
    # проверяем есть ли строка в БД с таким уникальным номером
    if read_d_from_db(d['unic_number']) is not None:
        update_case_db(d)  # UPDATE запрос, если есть
    else:
        insert_into_db(d)  # INSERT запрос, если нет


'''============================================================================
                    Функции для работы с базой данных контроля наполненности
============================================================================'''


# подготовка стандартного кортежа данных для добавления в БД
def prepare_data_for_fullness_db(d, new=False):
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
    # psy_check = False
    # logo_check = False

    # if 'exam_psy' in d:
    #     if 'icf_psy' in d:
    #         psy_check = True

    # if 'exam_logo' in d:
    #     if 'icf_logo' in d:
    #         logo_check = True

    if new:
        data = (d['unic_number'],
                d['check_line'])
    else:
        data = (d['check_line'],
                d['unic_number'])
    return data


# Функция создания базы данных наполненности
def create_fullness_db():
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
def insert_into_fullness_db(d):
    '''
    '''
    data_to_insert = prepare_data_for_fullness_db(d, True)

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
        print("[red]Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")


# Обновление записи в базе данных
def update_fullness_db(d):
    '''
    '''
    data_to_update = prepare_data_for_fullness_db(d)

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
def read_fullness_db(uin):
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


def write_fullness_table(d):
    if read_fullness_db(d['unic_number']) is not None:
        update_fullness_db(d)
    else:
        create_fullness_db()
        insert_into_fullness_db(d)


'''============================================================================
                    Функции для работы с базой данных функ.шкал
============================================================================'''


# подготовка стандартного кортежа данных для добавления в БД
def prepare_data_for_scale_db(d, new=False):
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
    # psy_check = False
    # logo_check = False

    # if 'exam_psy' in d:
    #     if 'icf_psy' in d:
    #         psy_check = True

    # if 'exam_logo' in d:
    #     if 'icf_logo' in d:
    #         logo_check = True

    if 'Шкалы' in d:
        if new:
            if 'NIHSS' in d:
                data = (d['unic_number'],
                        d['ШРМ'],
                        d['ШРМ_вып'],
                        d['mRs'],
                        d['mRs_вып'],
                        d['NIHSS'])
            else:
                data = (d['unic_number'],
                        d['ШРМ'],
                        d['ШРМ_вып'],
                        d['mRs'],
                        d['mRs_вып'],
                        '')
        else:
            if 'NIHSS' in d:
                data = (d['ШРМ'],
                        d['ШРМ_вып'],
                        d['mRs'],
                        d['mRs_вып'],
                        d['NIHSS'],
                        d['unic_number'])
            else:
                data = (d['ШРМ'],
                        d['ШРМ_вып'],
                        d['mRs'],
                        d['mRs_вып'],
                        '',
                        d['unic_number'])
    else:
        if new:
            data = (d['unic_number'],
                    '',
                    '',
                    '',
                    '',
                    '')
        else:
            data = ('',
                    '',
                    '',
                    '',
                    '',
                    d['unic_number'])
    return data


# Функция создания базы данных наполненности
def create_scale_db():
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            CREATE TABLE
            IF NOT EXISTS
            scale (
                case_id GUID PRIMARY KEY,
                RRS_adm TEXT,
                RRS_dis TEXT,
                mRs_adm TEXT,
                mRs_dis TEXT,
                nihss TEXT
                )''')
        con.commit()
        print("SQLite: создаем таблицу scale... ", end='')
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")


# Добавление данных в базу
def insert_into_scale_db(d):
    '''
    '''
    data_to_insert = prepare_data_for_scale_db(d, True)

    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            INSERT INTO scale (
                case_id,
                RRS_adm,
                RRS_dis,
                mRs_adm,
                mRs_dis,
                nihss)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', data_to_insert)
        con.commit()
        print("SQLite: данные успешно добавлены в таблицу шкал. ")
        cur.close()
    except sqlite3.Error as error:
        print("[red]Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")


# Обновление записи в базе данных
def update_scale_db(d):
    '''
    '''
    data_to_update = prepare_data_for_scale_db(d)

    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            UPDATE scale
            SET RRS_adm = ?,
                RRS_dis = ?,
                mRs_adm = ?,
                mRs_dis = ?,
                nihss = ?
            WHERE case_id = ?
            ''', data_to_update)
        con.commit()
        print("SQLite: данные успешно обновлены в таблице шкал. ")
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")


# чтение активных пациентов для списка на выписку
def read_scale_db(uin):
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            SELECT RRS_adm,
                   RRS_dis,
                   mRs_adm,
                   mRs_dis,
                   nihss
            FROM scale
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


def write_scale_table(d):
    if read_scale_db(d['unic_number']) is not None:
        update_scale_db(d)
    else:
        create_scale_db()
        insert_into_scale_db(d)
