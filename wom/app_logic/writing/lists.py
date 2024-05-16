

'''
'''
# импорты
import os
from docxtpl import DocxTemplate
from datetime import datetime
from prettytable import PrettyTable
from pathlib import Path
from numpy import unique

from wom.app_logic.db_func.db_omr import read_scale_db
from wom.app_logic.service_func import convert_date, datedif


PATH_TEMPLATES = 'wom/templates'
PATH_LISTS = 'CREATED/lists_of_patients'


# открыть папку со списками
def open_folder_patients_lists():
    os.startfile(Path(Path.cwd(), PATH_LISTS))


# создание списка текущих пациентов
def create_patients_list(data):
    '''
        type_hosp
        adm_date
        room_number
        full_name
        mkb10_ds
        doctor_name
        sicklist_check
        diet
        case_id
    '''
    column_1 = []
    column_2 = []
    full_patients_list = ''
    rooms = {
        '201': [2, []],
        '202': [2, []],
        '204': [5, []],
        '205': [2, []],
        '206': [3, []],
        '208': [2, []],
        '209': [2, []],
        '210': [6, []],
        '211': [2, []],
        '212': [2, []],
        '213': [2, []],
        '301': [2, []],
        '302': [2, []],
        '303': [5, []],
        '304': [2, []],
        '305': [2, []],
        '306': [5, []],
        '307': [5, []],
        '308': [3, []],
        '308A': [2, []],
        '309': [6, []],
        '310': [6, []],
        '311': [2, []],
        '312': [7, []],
        '313': [2, []],
        '315': [2, []]
    }

    check_2_flow = 0
    check_3_flow = 0
    check_9 = 0
    check_15 = 0
    check_ks = 0
    check_ds = 0

    for i in range(len(data)):
        today = datetime.now().strftime('%d.%m.%Y')
        day, month, year = data[i]['adm_date'].split('.')
        bed_days = datedif(data[i]['adm_date'], today)
        if data[i]['type_hosp'] == 'Круглосуточный стационар':
            bed_days -= 1
        if len(str(bed_days)) == 1:
            bed_days = f' {bed_days}'

        name = data[i]['full_name'].split(' ')
        if len(name) == 3:
            short_name = f'{name[0]} {name[1][0]}{name[2][0]}'
        else:
            short_name = name[0]

        day_str = f' {day}-{month} {bed_days}к/д  '  # 14 символов
        name_str = short_name
        while len(name_str) < 21:  # 21 символ
            name_str += ' '

        if data[i]['type_hosp'] == 'Круглосуточный стационар':
            type_h = 'КС'
            check_ks += 1
        elif data[i]['type_hosp'] == 'Дневной стационар':
            type_h = 'ДС'
            check_ds += 1
        else:
            type_h = '  '

        if len(data[i]['diet']) == 1:
            diet = f' {data[i]["diet"]}'
            check_9 += 1
        elif len(data[i]["diet"]) > 2:
            diet = data[i]["diet"][:2]
        else:
            diet = '15'
            check_15 += 1

        if data[i]['sicklist_check'] == '1':
            sicklist = 'ЛН'
        else:
            sicklist = '  '

        if data[i]['room_number'][0] == '2':
            check_2_flow += 1
        elif data[i]['room_number'][0] == '3':
            check_3_flow += 1

        last_str = f'{type_h}  {diet}  {sicklist}     '  # 15 символов

        string = day_str + name_str + last_str  # 50 символов

        if len(rooms[data[i]['room_number']][1]) < rooms[data[i]['room_number']][0]:
            rooms[data[i]['room_number']][1].append(string)

    for number in rooms:

        string_s = f'_____________/ № {number} ({rooms[number][0]}) \\____________________'
        while len(string_s) < 50:
            string_s += ' '

        empty_line = ''
        for i in range(5):
            empty_line += '          '

        if len(column_1) < 50:
            column_1.append(string_s)
            for i in range(patients := len(rooms[number][1])):
                column_1.append(rooms[number][1][i])

            if patients < rooms[number][0]:
                for i in range(rooms[number][0] - patients):
                    column_1.append(empty_line)
            column_1.append(empty_line)
        else:
            column_2.append(string_s)
            for i in range(patients := len(rooms[number][1])):
                column_2.append(rooms[number][1][i])

            if patients < rooms[number][0]:
                for i in range(rooms[number][0] - patients):
                    column_2.append(empty_line)
            column_2.append(empty_line)

    # print(column_1)
    # print(len(column_1))
    # print(column_2)
    # print(len(column_2))

    statistic = {
        'str_1': f'Всего в отделении: {len(data)} человек (КС {check_ks} / ДС {check_ds})',
        'str_2': f'       На 2 этаже: {check_2_flow}',
        'str_3': f'       На 3 этаже: {check_3_flow}',
        'str_4': f'Диета (стол)    9: {check_9}',
        'str_5': f'               15: {check_15}'
    }

    for i in range(7):
        column_1.append(empty_line)

    for i in range(len(statistic)):
        while len(statistic[f'str_{i + 1}']) < 50:
            statistic[f'str_{i + 1}'] += ' '
        column_1.append(statistic[f'str_{i + 1}'])

    if len(column_2) > len(column_1):
        for i in range(len(column_2) - len(column_1)):
            column_1.append(empty_line)
    elif len(column_1) > len(column_2):
        for i in range(len(column_1) - len(column_2)):
            column_2.append(empty_line)
    else:
        pass

    for i in range(len(column_2)):
        full_patients_list += f'{column_1[i]}{column_2[i]}\n'

    return full_patients_list


# создание списка пациентов на выписку
def create_patients_list_for_discharge(data):
    '''
    0 - type_hosp
    1 - adm_date
    2 - dis_date
    3 - room_number
    4 - full_name
    5 - doctor_name
    6 - sicklist_check
    7 - case_id
    '''
    patients = []
    dates = []
    docs = []
    for patient in data:
        # переназываем тип стационара
        if patient['type_hosp'] == 'Круглосуточный стационар':
            type_h = 'КС'
        elif patient['type_hosp'] == 'Дневной стационар':
            type_h = 'ДС'
        else:
            type_h = ''
        # создаем короткое имя
        name = patient['full_name'].split(' ')
        short_name = ''
        for i in range(len(name)):
            if i == 0:
                short_name += f'{name[i]} '
            else:
                short_name += name[i][0]
        # переназываем нужду в ЛН
        if patient['sicklist_check'] == '1':
            sicklist_check = 'ЕСТЬ'
        else:
            sicklist_check = ''

        if type_h == 'КС':
            bed_days = str(
                datedif(patient['adm_date'], patient['dis_date']) - 1)
        elif type_h == 'ДС':
            bed_days = str(
                datedif(patient['adm_date'], patient['dis_date']))
        else:
            bed_days = ''

        scale = read_scale_db(patient['case_id'])
        if scale is None:
            print(short_name)
            print(patient['case_id'])

        # print(short_name)
        # print(scale)

        pt_dict = {
            "type_hosp": type_h,
            "adm_date": convert_date(patient["adm_date"]),
            "dis_date": convert_date(patient["dis_date"]),
            "room_number": patient["room_number"],
            "pt_name": short_name,
            "doctor_name": patient["doctor_name"],
            "sicklist_check": sicklist_check,
            "bed_days": bed_days,
            "uin": patient["case_id"],
            "RRS": f"{scale[0]}-{scale[1]}",
            "mRs": f"{scale[2]}-{scale[3]}",
            "nihss": scale[4]
        }
        patients.append(pt_dict)
        dates.append(pt_dict['dis_date'])
        docs.append(pt_dict['doctor_name'])

    patients = sorted(
        patients,
        key=lambda x: x['pt_name'],
        reverse=False
    )
    patients = sorted(
        patients,
        key=lambda x: x['dis_date'],
        reverse=False
    )
    patients = sorted(
        patients,
        key=lambda x: x['room_number'],
        reverse=False
    )
    unique_dates = unique(dates)
    unique_docs = unique(docs)

    #
    table = PrettyTable()
    fields = ["№",
              "Дата выписки",
              "к/д",
              "Палата",
              "ФИО пациента",
              "ЛН",
              "Врач",
              "mRs",
              "ШРМ",
              "NIHSS"]
    table.field_names = fields

    for i in range(len(unique_dates)):
        check = 0
        for x in patients:
            if x['dis_date'] == unique_dates[i]:
                check += 1
                row = [check,
                       x['dis_date'].strftime('%d-%m-%Y'),
                       x['bed_days'],
                       x['room_number'],
                       x['pt_name'],
                       x['sicklist_check'],
                       x['doctor_name'],
                       x['mRs'],
                       x['RRS'],
                       x['nihss']]
                table.add_row(row)
        table.add_row(['', f'Всего: {check}', '', '', '', '', '', '', '', ''])
        table.add_row(['', '', '', '', '', '', '', '', '', ''])
        table.add_row(['', '', '', '', '', '', '', '', '', ''])
        if i != (len(unique_dates) - 1):
            table.add_row(['--', '------------', '---',
                           '------', '--------------------',
                           '----', '-------------', '---',
                           '---', '-----'])

    patients = sorted(
        patients,
        key=lambda x: x['dis_date'],
        reverse=False
    )

    table_doc = PrettyTable()
    table_doc.field_names = fields
    for i in range(len(unique_docs)):
        check = 0
        for x in patients:
            if x['doctor_name'] == unique_docs[i]:
                check += 1
                row = [check,
                       x['dis_date'].strftime('%d-%m-%Y'),
                       x['bed_days'],
                       x['room_number'],
                       x['pt_name'],
                       x['sicklist_check'],
                       x['doctor_name'],
                       x['mRs'],
                       x['RRS'],
                       x['nihss']]
                table_doc.add_row(row)
        table_doc.add_row(['', f'Всего: {check}', '',
                           '', '', '', '', '', '', ''])
        table_doc.add_row(['', '', '', '', '', '', '', '', '', ''])
        table_doc.add_row(['', '', '', '', '', '', '', '', '', ''])
        if i != (len(unique_docs) - 1):
            table_doc.add_row(['--', '------------', '---',
                               '------', '--------------------',
                               '----', '-------------', '---',
                               '---', '-----'])

    return {
        'simple': table,
        'docs': table_doc
    }


# создание списков пациентов для каждого врача (для обхода)
def create_doc_lists(data):
    '''
    type_hosp,
    adm_date,
    room_number,
    full_name,
    mkb10_ds,
    doctor_name,
    sicklist_check,
    diet,
    case_id,
    dis_date
    '''
    today = datetime.now().strftime('%d.%m.%Y')

    patients = []
    doctors = []

    for patient in data:
        # переназываем нужду в ЛН
        if patient["sicklist_check"] == '1':
            sicklist_check = '(ЛН)'
        else:
            sicklist_check = ''

        if patient['type_hosp'] == 'Круглосуточный стационар':
            bed_days = str(datedif(patient['adm_date'],
                                   patient['dis_date']) - 1)
            bed_days_now = str(datedif(patient['adm_date'], today) - 1)
        elif patient[0] == 'Дневной стационар':
            bed_days = str(datedif(patient['adm_date'],
                                   patient['dis_date']))
            bed_days_now = str(datedif(patient['adm_date'], today))
        else:
            bed_days = ''
            bed_days_now = ''

        pt_dict = {
            'room_number': patient['room_number'],
            'full_name': patient['full_name'],
            'mkb10': patient['mkb10_ds'],
            'doctor_name': patient['doctor_name'],
            'sicklist_check': sicklist_check,
            'dis_date': patient['dis_date'],
            'adm_date': patient['adm_date'],
            'bed_days': bed_days,
            'bed_days_now': bed_days_now
        }

        patients.append(pt_dict)
        doctors.append(pt_dict['doctor_name'])

    patients = sorted(
        patients,
        key=lambda x: x['room_number'],
        reverse=False
    )

    unique_doctors = unique(doctors)

    doc_pt = []
    for i in range(len(unique_doctors)):
        doc_pt.append([])
        for x in patients:
            if x['doctor_name'] == unique_doctors[i]:
                doc_pt[i].append(x)

    full_text = ''

    for i in range(len(doc_pt)):
        doc_text = ''
        table = PrettyTable()
        fields = ["Пациент",
                  "Заметка"]
        table.field_names = fields
        header = f"\tСписок пациентов на {today}, "\
                 f"врач: {doc_pt[i][0]['doctor_name']}, "\
                 f"кол-во пациентов: {len(doc_pt[i])}\n"
        doc_text += header

        room_now = ''
        room_prev = ''
        room_count = 0
        patient_count = 0
        empty_lines = 0

        for pt in doc_pt[i]:

            room_now = pt['room_number']
            if room_now != room_prev:
                if room_prev != '':
                    strings = patient_count * 5 + room_count + 4
                    if 0 <= (x := (82 - strings)) <= 15:
                        while strings < 82:
                            table.add_row(['', ''])
                            strings += 1
                        empty_lines += x

                    room_count += 1
                    table.add_row([
                        f'------------- Палата № {room_now} -------------',
                        '------------------------------------------'])
                else:
                    room_count += 1
                    table.add_row([f'Палата № {room_now}',
                                   ''])
            else:
                pass

            strings = patient_count * 5 + room_count + empty_lines + 4
            if 0 <= (x := (82 - strings)) <= 3:
                while strings < 82:
                    table.add_row(['', ''])
                    strings += 1
                empty_lines += x

            patient_count += 1
            pt_text_1 = f"{pt['full_name']} {pt['sicklist_check']}"
            pt_text_2 = f"{pt['mkb10']}; пост.:{pt['adm_date']}, "\
                        f"{pt['bed_days_now']} к/д;"
            pt_text_3 = f"       вып.:{pt['dis_date']}, {pt['bed_days']} к/д;"
            table.add_row([pt_text_1, ''])
            table.add_row([pt_text_2, ''])
            table.add_row([pt_text_3, ''])
            table.add_row(['', ''])
            # table.add_row(['', ''])
            table.add_row(['', '------------------------------------------'])

            room_prev = room_now

        strings = len(doc_pt[i]) * 5 + room_count + empty_lines + 5
        while strings < 163:
            table.add_row(['', ''])
            strings += 1

        doc_text += str(table) + '\n'
        full_text += doc_text + '\t\t\t\t\t\tWorld of Medicine\n'

    return full_text[:-1]


def creating_file_pt_list(d, filetype):
    '''
    принимает d - словарь со значениями
              type

    силами docxtpl.DocxTemplate создает документы .docx
    на основе словаря и списка шаблонов templates

    формирует файловую систему хранения созданных
    текстовых документов с помощью os.makedirs()

    ничего не возвращает
    '''
    today = datetime.now().strftime('%d-%m-%Y')

    if filetype == 'today_list':
        d['Заголовок'] = f'{today} - Список пациентов'
    elif filetype == 'discharge':
        d['Заголовок'] = f'{today} - Список пациентов на выписку'
    # создание имени нового файла и пути для его сохранения
    docName = f"{d['Заголовок']}.docx"
    # формируем окончательное имя файла
    filepath = Path(Path.cwd(), PATH_LISTS, docName)

    # создаем документ на основе шаблона
    doc = DocxTemplate(Path(Path.cwd(),
                            PATH_TEMPLATES,
                            'список_пациентов.docx'))
    # создание файла по шаблону на основе словаря
    doc.render(d)
    # # создаем папки на пути к файлу
    os.makedirs(Path(Path.cwd(), PATH_LISTS), exist_ok=True)
    # сохранение файла по указанному пути, с указанным именем
    doc.save(filepath)


def creating_file_doc_lists(d):
    '''
    принимает d - словарь со значениями

    силами docxtpl.DocxTemplate создает документы .docx
    на основе словаря и списка шаблонов templates

    ничего не возвращает
    '''
    today = datetime.now().strftime('%d-%m-%Y')

    # создание имени нового файла и пути для его сохранения
    docName = f"{today} - Списки для обхода.docx"
    # формируем окончательное имя файла
    filepath = Path(Path.cwd(), PATH_LISTS, docName)

    # создаем документ на основе шаблона
    doc = DocxTemplate(Path(Path.cwd(),
                            PATH_TEMPLATES,
                            'списки для обхода.docx'))
    # создание файла по шаблону на основе словаря
    doc.render(d)
    # # создаем папки на пути к файлу
    os.makedirs(Path(Path.cwd(), PATH_LISTS), exist_ok=True)
    # сохранение файла по указанному пути, с указанным именем
    doc.save(filepath)
