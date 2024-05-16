import sqlite3
from wom.settings.paths import DATABASE_TEMPLATES
'''============================================================================
        Функции для работы с базой данных шаблонов соматического статуса
============================================================================'''


DATABASE = DATABASE_TEMPLATES


# Функция создания базы данных для хранения
# шаблонов соматического статуса
def create_db_obj_templates():
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            CREATE TABLE
            IF NOT EXISTS
            obj_templates (
                template_name TEXT PRIMARY KEY,
                PtGeneralState TEXT,
                PtSkinState_1 TEXT,
                PtSkinState_2 TEXT,
                PtLymphnode TEXT,
                PtMucousMembr_1 TEXT,
                PtBreathing_1 TEXT,
                PtBreathing_2 TEXT,
                PtBreathing_3 TEXT,
                PtWheezingChoice TEXT,
                PtWheezing_1 TEXT,
                PtWheezing_2 TEXT,
                PtWheezing_3 TEXT,
                PtDyspneaChoice TEXT,
                PtDyspnea_1 TEXT,
                PtDyspnea_2 TEXT,
                PtDyspnea_3 TEXT,
                PtHearthTone_1 TEXT,
                PtHearthTone_2 TEXT,
                PtHearthTone_3 TEXT,
                PtHearthNoiseChoice TEXT,
                PtHearthNoise TEXT,
                PtStomach_1 TEXT,
                PtStomach_2 TEXT,
                PtStomach_3 TEXT,
                PtDefecation_1 TEXT,
                PtDefecation_2 TEXT,
                PtDefecation_3 TEXT,
                PtUrination_1 TEXT,
                PtUrination_2 TEXT,
                PtUrination_3 TEXT,
                PtStObjOther TEXT
            )''')
        con.commit()
        print("SQLite: создаем таблицу шаблонов ObjSt. ")
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")


# чтение шаблона соматического статуса по имени
def read_db_obj_template_data(template_name):
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        query = '''
            SELECT PtGeneralState,
                   PtSkinState_1,
                   PtSkinState_2,
                   PtLymphnode,
                   PtMucousMembr_1,
                   PtBreathing_1,
                   PtBreathing_2,
                   PtBreathing_3,
                   PtWheezingChoice,
                   PtWheezing_1,
                   PtWheezing_2,
                   PtWheezing_3,
                   PtDyspneaChoice,
                   PtDyspnea_1,
                   PtDyspnea_2,
                   PtDyspnea_3,
                   PtHearthTone_1,
                   PtHearthTone_2,
                   PtHearthTone_3,
                   PtHearthNoiseChoice,
                   PtHearthNoise,
                   PtStomach_1,
                   PtStomach_2,
                   PtStomach_3,
                   PtDefecation_1,
                   PtDefecation_2,
                   PtDefecation_3,
                   PtUrination_1,
                   PtUrination_2,
                   PtUrination_3,
                   PtStObjOther
            FROM obj_templates WHERE template_name = ?'''
        cur.execute(query, template_name)
        data = cur.fetchone()
        print('SQLite: чтение шаблона ObjSt... Ok')
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
        return data


# чтение списка шаблонов соматического статуса
def read_db_obj_template_list():
    '''
    '''
    try:
        good_data = ['']
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        query = '''SELECT template_name
                   FROM obj_templates'''
        cur.execute(query)
        data = cur.fetchall()
        if data is not None:
            for i in range(len(data)):
                good_data.append(data[i][0])
        print('SQLite: чтение списка шаблонов ObjSt... Ok')
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
        return good_data


# Добавление нового шаблона сом.статуса в базу
def insert_obj_template_into_db(data_to_insert):
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            INSERT INTO obj_templates (
                template_name,
                PtGeneralState,
                PtSkinState_1,
                PtSkinState_2,
                PtLymphnode,
                PtMucousMembr_1,
                PtBreathing_1,
                PtBreathing_2,
                PtBreathing_3,
                PtWheezingChoice,
                PtWheezing_1,
                PtWheezing_2,
                PtWheezing_3,
                PtDyspneaChoice,
                PtDyspnea_1,
                PtDyspnea_2,
                PtDyspnea_3,
                PtHearthTone_1,
                PtHearthTone_2,
                PtHearthTone_3,
                PtHearthNoiseChoice,
                PtHearthNoise,
                PtStomach_1,
                PtStomach_2,
                PtStomach_3,
                PtDefecation_1,
                PtDefecation_2,
                PtDefecation_3,
                PtUrination_1,
                PtUrination_2,
                PtUrination_3,
                PtStObjOther)
            VALUES (?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?)
            ''', data_to_insert)
        con.commit()
        msg = f"SQLite: шаблон "\
              f"({data_to_insert[0]}) "\
              f"для ObjSt успешно добавлен. "
        print(msg)
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")


# Обновление записи в базе данных
def update_obj_template_db(data_to_update):
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            UPDATE obj_templates
            SET PtGeneralState = ?,
                PtSkinState_1 = ?,
                PtSkinState_2 = ?,
                PtLymphnode = ?,
                PtMucousMembr_1 = ?,
                PtBreathing_1 = ?,
                PtBreathing_2 = ?,
                PtBreathing_3 = ?,
                PtWheezingChoice = ?,
                PtWheezing_1 = ?,
                PtWheezing_2 = ?,
                PtWheezing_3 = ?,
                PtDyspneaChoice = ?,
                PtDyspnea_1 = ?,
                PtDyspnea_2 = ?,
                PtDyspnea_3 = ?,
                PtHearthTone_1 = ?,
                PtHearthTone_2 = ?,
                PtHearthTone_3 = ?,
                PtHearthNoiseChoice = ?,
                PtHearthNoise = ?,
                PtStomach_1 = ?,
                PtStomach_2 = ?,
                PtStomach_3 = ?,
                PtDefecation_1 = ?,
                PtDefecation_2 = ?,
                PtDefecation_3 = ?,
                PtUrination_1 = ?,
                PtUrination_2 = ?,
                PtUrination_3 = ?,
                PtStObjOther = ?
            WHERE template_name = ?
            ''', data_to_update)
        con.commit()
        msg = f"SQLite: шаблон ObjSt "\
              f"({data_to_update[-1]}) "\
              f"успешно обновлен. "
        print(msg)
        cur.close()
        # делаем из множества строку для избежания ошибок записи и чтения
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")


# Добавление нового шаблона сом.статуса в базу
def insert_normal_obj_template_into_db():
    '''
    '''
    try:
        data_to_insert = (
            'Норма',
            'удовлетворительное',
            'физиологические',
            'высыпаний нет',
            'не увеличены',
            'физиологической окраски',
            'свободное, через нос',
            'везикулярное',
            'проводится во все отделы',
            'нет',
            '-----',
            '-----',
            '-----',
            'нет',
            '-----',
            '-----',
            '-----',
            'ясные',
            'ритмичные',
            '-----',
            'нет',
            'не выслушиваются',
            'ненапряжен',
            'безболезненный',
            'участвует в акте дыхания',
            'оформленный',
            'регулярный',
            'ежедневный',
            'контролирует',
            'достаточное',
            '-----',
            '')
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            INSERT INTO obj_templates (
                template_name,
                PtGeneralState,
                PtSkinState_1,
                PtSkinState_2,
                PtLymphnode,
                PtMucousMembr_1,
                PtBreathing_1,
                PtBreathing_2,
                PtBreathing_3,
                PtWheezingChoice,
                PtWheezing_1,
                PtWheezing_2,
                PtWheezing_3,
                PtDyspneaChoice,
                PtDyspnea_1,
                PtDyspnea_2,
                PtDyspnea_3,
                PtHearthTone_1,
                PtHearthTone_2,
                PtHearthTone_3,
                PtHearthNoiseChoice,
                PtHearthNoise,
                PtStomach_1,
                PtStomach_2,
                PtStomach_3,
                PtDefecation_1,
                PtDefecation_2,
                PtDefecation_3,
                PtUrination_1,
                PtUrination_2,
                PtUrination_3,
                PtStObjOther)
            VALUES (?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?)
            ''', data_to_insert)
        con.commit()
        print("SQLite: шаблон ObjSt (Норма) успешно добавлен... ", end='')
        cur.close()
    except sqlite3.Error:
        print("SQLite: шаблон ObjSt (Норма) уже есть в БД... ", end='')
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")
