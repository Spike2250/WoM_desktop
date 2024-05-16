import sqlite3
from wom.settings.paths import DATABASE_TEMPLATES
'''============================================================================
        Функции для работы с базой данных шаблонов неврологического статуса
============================================================================'''


DATABASE = DATABASE_TEMPLATES


# Функция создания базы данных для хранения
# шаблонов неврологического статуса
def create_db_neur_templates():
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            CREATE TABLE
            IF NOT EXISTS
            neur_templates (
                template_name TEXT PRIMARY KEY,
                Conscious TEXT,
                GCS TEXT,
                RASS TEXT,
                Contact TEXT,
                Orientation TEXT,
                MeningealSymp_1 TEXT,
                MeningealSymp_2 TEXT,
                MeningealSymp_3 TEXT,
                Speech_1 TEXT,
                Speech_2 TEXT,
                Speech_3 TEXT,
                PelvicFuntion TEXT,
                Smell TEXT,
                VisualAcuity TEXT,
                Fields TEXT,
                Pupils TEXT,
                Accomodation TEXT,
                Photoreaction TEXT,
                Convergension TEXT,
                EyeballMove TEXT,
                EyeballParesis TEXT,
                Ptosis TEXT,
                Nystagmus TEXT,
                FaceSensitivity TEXT,
                Branches TEXT,
                Zelder TEXT,
                Symmetry TEXT,
                face_Other TEXT,
                Hearing TEXT,
                CentralVertigo TEXT,
                Phonation TEXT,
                SoftPalate TEXT,
                Swallowing TEXT,
                Food TEXT,
                Dysarthria TEXT,
                Dysarthria_power TEXT,
                cranial_11 TEXT,
                cranial_12 TEXT,
                Moving_limbs TEXT,
                Moving_joints TEXT,
                Moving_spine TEXT,
                MRC_R_A_P TEXT,
                MRC_R_A_D TEXT,
                MRC_R_L_P TEXT,
                MRC_R_L_D TEXT,
                MRC_L_A_P TEXT,
                MRC_L_A_D TEXT,
                MRC_L_L_P TEXT,
                MRC_L_L_D TEXT,
                MuscleTonus_1 TEXT,
                MuscleTonus_2 TEXT,
                Ash_R_A_P TEXT,
                Ash_R_A_D TEXT,
                Ash_R_L_P TEXT,
                Ash_R_L_D TEXT,
                Ash_L_A_P TEXT,
                Ash_L_A_D TEXT,
                Ash_L_L_P TEXT,
                Ash_L_L_D TEXT,
                Arms_reflex_1 TEXT,
                Arms_reflex_2 TEXT,
                Legs_reflex_1 TEXT,
                Legs_reflex_2 TEXT,
                Pathology_reflex TEXT,
                MuscleTrofic TEXT,
                Sensitivity_1 TEXT,
                Sensitivity_2 TEXT,
                Sensitivity TEXT,
                Coordination_1 TEXT,
                Coordination_2 TEXT,
                Coordination TEXT,
                Extrapyramid_1 TEXT,
                Extrapyramid_2 TEXT,
                Extrapyramid_3 TEXT,
                EpilepticStatus TEXT,
                FuncStatus_common TEXT,
                FuncStatus_walking TEXT,
                FuncStatus_walking_type TEXT,
                FuncStatus_motorics TEXT,
                FuncStatus_dressing TEXT,
                FuncStatus_stairway TEXT,
                FuncStatus_eating TEXT,
                FuncStatus_writing TEXT,
                FuncStatus_reading TEXT,
                FuncStatus TEXT,
                other TEXT
            )''')
        con.commit()
        print("SQLite: создаем таблицу шаблонов NeurSt. ")
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")


# чтение шаблона неврологического статуса по имени
def read_db_neur_template_data(template_name):
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        query = '''SELECT Conscious,
                          GCS,
                          RASS,
                          Contact,
                          Orientation,
                          MeningealSymp_1,
                          MeningealSymp_2,
                          MeningealSymp_3,
                          Speech_1,
                          Speech_2,
                          Speech_3,
                          PelvicFuntion,
                          Smell,
                          VisualAcuity,
                          Fields,
                          Pupils,
                          Accomodation,
                          Photoreaction,
                          Convergension,
                          EyeballMove,
                          EyeballParesis,
                          Ptosis,
                          Nystagmus,
                          FaceSensitivity,
                          Branches,
                          Zelder,
                          Symmetry,
                          face_Other,
                          Hearing,
                          CentralVertigo,
                          Phonation,
                          SoftPalate,
                          Swallowing,
                          Food,
                          Dysarthria,
                          Dysarthria_power,
                          cranial_11,
                          cranial_12,
                          Moving_limbs,
                          Moving_joints,
                          Moving_spine,
                          MRC_R_A_P,
                          MRC_R_A_D,
                          MRC_R_L_P,
                          MRC_R_L_D,
                          MRC_L_A_P,
                          MRC_L_A_D,
                          MRC_L_L_P,
                          MRC_L_L_D,
                          MuscleTonus_1,
                          MuscleTonus_2,
                          Ash_R_A_P,
                          Ash_R_A_D,
                          Ash_R_L_P,
                          Ash_R_L_D,
                          Ash_L_A_P,
                          Ash_L_A_D,
                          Ash_L_L_P,
                          Ash_L_L_D,
                          Arms_reflex_1,
                          Arms_reflex_2,
                          Legs_reflex_1,
                          Legs_reflex_2,
                          Pathology_reflex,
                          MuscleTrofic,
                          Sensitivity_1,
                          Sensitivity_2,
                          Sensitivity,
                          Coordination_1,
                          Coordination_2,
                          Coordination,
                          Extrapyramid_1,
                          Extrapyramid_2,
                          Extrapyramid_3,
                          EpilepticStatus,
                          FuncStatus_common,
                          FuncStatus_walking,
                          FuncStatus_walking_type,
                          FuncStatus_motorics,
                          FuncStatus_dressing,
                          FuncStatus_stairway,
                          FuncStatus_eating,
                          FuncStatus_writing,
                          FuncStatus_reading,
                          FuncStatus,
                          other
                   FROM neur_templates WHERE template_name = ?'''
        cur.execute(query, template_name)
        data = cur.fetchone()
        print('SQLite: чтение шаблона NeurSt... Ok')
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


# чтение списка шаблонов неврологического статуса
def read_db_neur_template_list():
    '''
    '''
    try:
        good_data = ['']
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        query = '''SELECT template_name
                   FROM neur_templates'''
        cur.execute(query)
        data = cur.fetchall()
        if data is not None:
            for i in range(len(data)):
                good_data.append(data[i][0])
        print('SQLite: чтение списка шаблонов NeurSt... Ok')
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


# Добавление нового шаблона в базу
def insert_neur_template_into_db(data_to_insert):
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            INSERT INTO neur_templates (
                template_name,
                Conscious,
                GCS,
                RASS,
                Contact,
                Orientation,
                MeningealSymp_1,
                MeningealSymp_2,
                MeningealSymp_3,
                Speech_1,
                Speech_2,
                Speech_3,
                PelvicFuntion,
                Smell,
                VisualAcuity,
                Fields,
                Pupils,
                Accomodation,
                Photoreaction,
                Convergension,
                EyeballMove,
                EyeballParesis,
                Ptosis,
                Nystagmus,
                FaceSensitivity,
                Branches,
                Zelder,
                Symmetry,
                face_Other,
                Hearing,
                CentralVertigo,
                Phonation,
                SoftPalate,
                Swallowing,
                Food,
                Dysarthria,
                Dysarthria_power,
                cranial_11,
                cranial_12,
                Moving_limbs,
                Moving_joints,
                Moving_spine,
                MRC_R_A_P,
                MRC_R_A_D,
                MRC_R_L_P,
                MRC_R_L_D,
                MRC_L_A_P,
                MRC_L_A_D,
                MRC_L_L_P,
                MRC_L_L_D,
                MuscleTonus_1,
                MuscleTonus_2,
                Ash_R_A_P,
                Ash_R_A_D,
                Ash_R_L_P,
                Ash_R_L_D,
                Ash_L_A_P,
                Ash_L_A_D,
                Ash_L_L_P,
                Ash_L_L_D,
                Arms_reflex_1,
                Arms_reflex_2,
                Legs_reflex_1,
                Legs_reflex_2,
                Pathology_reflex,
                MuscleTrofic,
                Sensitivity_1,
                Sensitivity_2,
                Sensitivity,
                Coordination_1,
                Coordination_2,
                Coordination,
                Extrapyramid_1,
                Extrapyramid_2,
                Extrapyramid_3,
                EpilepticStatus,
                FuncStatus_common,
                FuncStatus_walking,
                FuncStatus_walking_type,
                FuncStatus_motorics,
                FuncStatus_dressing,
                FuncStatus_stairway,
                FuncStatus_eating,
                FuncStatus_writing,
                FuncStatus_reading,
                FuncStatus,
                other)
            VALUES (?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?)
            ''', data_to_insert)
        con.commit()
        msg = f"SQLite: новый шаблон Невр.статуса "\
              f"({data_to_insert[0]}) успешно добавлен. "
        print(msg)
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")


# Обновление записи в базе данных
def update_neur_template_db(data_to_update):
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            UPDATE neur_templates
            SET Conscious = ?,
                GCS = ?,
                RASS = ?,
                Contact = ?,
                Orientation = ?,
                MeningealSymp_1 = ?,
                MeningealSymp_2 = ?,
                MeningealSymp_3 = ?,
                Speech_1 = ?,
                Speech_2 = ?,
                Speech_3 = ?,
                PelvicFuntion = ?,
                Smell = ?,
                VisualAcuity = ?,
                Fields = ?,
                Pupils = ?,
                Accomodation = ?,
                Photoreaction = ?,
                Convergension = ?,
                EyeballMove = ?,
                EyeballParesis = ?,
                Ptosis = ?,
                Nystagmus = ?,
                FaceSensitivity = ?,
                Branches = ?,
                Zelder = ?,
                Symmetry = ?,
                face_Other = ?,
                Hearing = ?,
                CentralVertigo = ?,
                Phonation = ?,
                SoftPalate = ?,
                Swallowing = ?,
                Food = ?,
                Dysarthria = ?,
                Dysarthria_power = ?,
                cranial_11 = ?,
                cranial_12 = ?,
                Moving_limbs = ?,
                Moving_joints = ?,
                Moving_spine = ?,
                MRC_R_A_P = ?,
                MRC_R_A_D = ?,
                MRC_R_L_P = ?,
                MRC_R_L_D = ?,
                MRC_L_A_P = ?,
                MRC_L_A_D = ?,
                MRC_L_L_P = ?,
                MRC_L_L_D = ?,
                MuscleTonus_1 = ?,
                MuscleTonus_2 = ?,
                Ash_R_A_P = ?,
                Ash_R_A_D = ?,
                Ash_R_L_P = ?,
                Ash_R_L_D = ?,
                Ash_L_A_P = ?,
                Ash_L_A_D = ?,
                Ash_L_L_P = ?,
                Ash_L_L_D = ?,
                Arms_reflex_1 = ?,
                Arms_reflex_2 = ?,
                Legs_reflex_1 = ?,
                Legs_reflex_2 = ?,
                Pathology_reflex = ?,
                MuscleTrofic = ?,
                Sensitivity_1 = ?,
                Sensitivity_2 = ?,
                Sensitivity = ?,
                Coordination_1 = ?,
                Coordination_2 = ?,
                Coordination = ?,
                Extrapyramid_1 = ?,
                Extrapyramid_2 = ?,
                Extrapyramid_3 = ?,
                EpilepticStatus = ?,
                FuncStatus_common = ?,
                FuncStatus_walking = ?,
                FuncStatus_walking_type = ?,
                FuncStatus_motorics = ?,
                FuncStatus_dressing = ?,
                FuncStatus_stairway = ?,
                FuncStatus_eating = ?,
                FuncStatus_writing = ?,
                FuncStatus_reading = ?,
                FuncStatus = ?,
                other = ?
            WHERE template_name = ?
            ''', data_to_update)
        con.commit()
        msg = f"SQLite: шаблон Невр.статуса "\
              f"({data_to_update[-1]}) успешно обновлен... "
        print(msg)
        cur.close()
        # делаем из множества строку для избежания ошибок записи и чтения
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")


# Добавление шаблона нормы невр.статуса в базу
def insert_normal_neur_template_into_db():
    '''
    '''
    try:
        data_to_insert = (
            'Норма',
            'Ясное',
            '15',
            '0',
            'продуктивный',
            'всесторонне ориентирован',
            'отрицательные',
            '-----',
            '-----',
            'сохранена',
            '-----',
            '-----',
            'сохранены',
            'сохранено',
            'сохранена',
            'сохранены',
            'D=S, ~3мм',
            'сохранена',
            'живая',
            'сохранена',
            'в полном объеме',
            'нет',
            'нет',
            'нет',
            'сохранена',
            'не поражены',
            'нарушений нет',
            'симметричны',
            '-----',
            'сохранен',
            'отсутствует',
            'сохранена',
            'подвижно',
            'не нарушено',
            'через рот',
            'отсутствует',
            '-----',
            'сохранена',
            'по средней линии',
            'в полном объеме',
            'в полном объеме',
            'в полном объеме',
            '5',
            '5',
            '5',
            '5',
            '5',
            '5',
            '5',
            '5',
            'физиологический',
            '-----',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            'D = S',
            'живые',
            'D = S',
            'живые',
            'не вызываются',
            'не изменена',
            'сохранена',
            '-----',
            '',
            'ПНП, ПКП - без промахивания',
            'В п.Ромберга - устойчив',
            '',
            'не нарушена',
            '-----',
            '-----',
            'припадков нет',
            'не ограничен в самообслуживании',
            'не ограничена, без дополнительной опоры',
            'не изменена',
            'сохранена',
            'самостоятельно',
            'самостоятельно, без ограничений',
            'самостоятельно, без ограничений',
            'сохранено',
            'сохранено',
            '',
            '')

        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            INSERT INTO neur_templates (
                template_name,
                Conscious,
                GCS,
                RASS,
                Contact,
                Orientation,
                MeningealSymp_1,
                MeningealSymp_2,
                MeningealSymp_3,
                Speech_1,
                Speech_2,
                Speech_3,
                PelvicFuntion,
                Smell,
                VisualAcuity,
                Fields,
                Pupils,
                Accomodation,
                Photoreaction,
                Convergension,
                EyeballMove,
                EyeballParesis,
                Ptosis,
                Nystagmus,
                FaceSensitivity,
                Branches,
                Zelder,
                Symmetry,
                face_Other,
                Hearing,
                CentralVertigo,
                Phonation,
                SoftPalate,
                Swallowing,
                Food,
                Dysarthria,
                Dysarthria_power,
                cranial_11,
                cranial_12,
                Moving_limbs,
                Moving_joints,
                Moving_spine,
                MRC_R_A_P,
                MRC_R_A_D,
                MRC_R_L_P,
                MRC_R_L_D,
                MRC_L_A_P,
                MRC_L_A_D,
                MRC_L_L_P,
                MRC_L_L_D,
                MuscleTonus_1,
                MuscleTonus_2,
                Ash_R_A_P,
                Ash_R_A_D,
                Ash_R_L_P,
                Ash_R_L_D,
                Ash_L_A_P,
                Ash_L_A_D,
                Ash_L_L_P,
                Ash_L_L_D,
                Arms_reflex_1,
                Arms_reflex_2,
                Legs_reflex_1,
                Legs_reflex_2,
                Pathology_reflex,
                MuscleTrofic,
                Sensitivity_1,
                Sensitivity_2,
                Sensitivity,
                Coordination_1,
                Coordination_2,
                Coordination,
                Extrapyramid_1,
                Extrapyramid_2,
                Extrapyramid_3,
                EpilepticStatus,
                FuncStatus_common,
                FuncStatus_walking,
                FuncStatus_walking_type,
                FuncStatus_motorics,
                FuncStatus_dressing,
                FuncStatus_stairway,
                FuncStatus_eating,
                FuncStatus_writing,
                FuncStatus_reading,
                FuncStatus,
                other)
            VALUES (?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?)
            ''', data_to_insert)
        con.commit()
        print("SQLite: шаблон NeurSt (Норма) успешно добавлен.")
        cur.close()
    except sqlite3.Error:
        print("SQLite: шаблон NeurSt (Норма) уже есть в БД.")
    finally:
        if con:
            con.close()
            print("    Соединение с SQLite успешно закрыто.")
