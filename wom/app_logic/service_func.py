from datetime import datetime
import json
from pathlib import Path
from decimal import Decimal


# из "дд.мм.гггг:" в datetime.datetime
def convert_date(date_string):
    # создаем список значений даты  | x = [дд, мм, гггг]
    x = [int(s) for s in date_string.split('.')]
    date = datetime(x[2], x[1], x[0])  # конвертируем формат
    return date


# запись словаря в json
def json_recording(d, type_=None):
    # записываем словарь в отдельный файл в формате json
    json_dict_name = f'{d["unic_number"]}.json'
    default_path = 'AWP_WoM/wom/JSON'
    folder_path = default_path if type_ is None else f'{default_path}/{type_}'
    json_file_path = Path(Path.cwd(), folder_path, json_dict_name)
    with open(json_file_path, 'w') as file:
        json.dump(d, file, indent=2)


def calc_percent_fullness(fullness, bta=False):
    if not bta:
        check_max = 13  # пока 13 с связи с недоделанными 3 разделами
    else:
        check_max = 7
    check = 0
    for i in fullness[0]:
        if i == '1':
            check += 1
    percent = Decimal(check * 100 / check_max).quantize(Decimal('1'))
    return int(percent)


# РАЗНДАТ (для дней нетрудоспособности)
def datedif(date1, date2):
    ''' Функция принимает 2 числа в формате 'дд.мм.гггг'
        date1 дата от которой считаем
        date2 дата до которой считаем

        Вычисление количества дней между двумя датами с
        включением первого и последнего дня
        Например для вычисление количества дней нетрудоспособности
        от дня открытия больничного листа до даты ВК
    '''
    # конвертируем даты в datetime.datetime
    date1, date2 = convert_date(date1), convert_date(date2)

    delta = date2 - date1  # считаем разницу дат
    # выводим разницу дат + 1 (для включения дня отсчета)
    return delta.days + 1


def create_mkb_nmu_dict():
    # import json-файлов с МКБ-10 и Номенклатурой мед.услуг
    file_path_mkb10 = Path(__file__).parent / "handbooks/mkb10.json"
    file_path_nmu = Path(__file__).parent / "handbooks/nmu.json"

    with open(file_path_mkb10, 'r') as file:
        mkb10 = json.load(file)
    with open(file_path_nmu, 'r') as file:
        nmu = json.load(file)

    return mkb10, nmu


# расшифровка МКБ и НМУ (подписи для кодов)
def add_mkb10_nmu(d):
    '''
    Функция добавления к словарю расшифровок услуги и кода по МКБ-10
    '''
    mkb10, nmu = create_mkb_nmu_dict()
    # Добавляем расшифровки
    d['услуга_расшифровка'] = nmu[d['услуга']]
    d['МКБ10_расшифровка'] = mkb10[d['МКБ']]


def create_short_name(full_name):
    '''
    Создает из строки 'Иванов Иван Иванович'
         'Иванов_ИИ'
    '''
    # Разделяем строку на список слов
    splited_name = full_name.split(' ')
    short_name = ''
    for i in range(len(splited_name)):
        if i == 0:  # Берем целиком первое слово
            short_name = splited_name[i] + ' '
        else:  # И по первой букве от остальных
            short_name = short_name + splited_name[i][0]

    return short_name


# посчитать возраст на сегодня()
def count_age(d):
    '''
    Получение возраста в полных годах
        от даты рождения до сегодня (date.today())
    '''
    today = datetime.today()
    birthday = convert_date(d['дата_рождения'])
    age = today.year - birthday.year
    if today.month < birthday.month:
        age -= 1
    elif today.month == birthday.month and today.day < birthday.day:
        age -= 1

    return str(age)


def calc_BMI(height, weight):
    ''' Расчет Индекса массы тела по Кеттле, округление до сотых

        функция принимает 2 аргумента:
        Рост      int  м или см
        Вес       int  кг

        Возвращает 4 значения:
        Результат в виде формата Decimal округленного до сотых
        Единицы измерения ИМТ (кг/м2)
        Заключение по ИМТ (степень Ожирения)
        'Флажок' - True, если значение больше
                   определенной границы (по умолчанию 30 кг/м2)
                   для запроса на внесение в диагноз
    '''
    result = None
    units = 'кг/м2'
    questionDS = False

    if height > 3:  # Если рост больше 3, считаем что значение в сантиметрах
        height /= 100  # Переводим сантиметры в метры

    result = weight / (height ** 2)   # Расчет Индекса массы тела по Кеттле

    result = Decimal(result)  # Преобразование числа в формат Decimal
    result = result.quantize(Decimal("1.00"))   # Округление до сотых

    # заключение по результату ИМТ
    if result < 18:
        conclusion = f'Дефицит массы тела (ИМТ = {result}{units}).'
    elif 18 <= result < 25:
        conclusion = f'Нормальная масса тела (ИМТ = {result}{units}).'
    elif 25 <= result < 30:
        conclusion = f'Избыточная масса тела (ИМТ = {result}{units}).'
    elif 30 <= result < 35:
        conclusion = f'Ожирение I ст. (ИМТ = {result}{units}).'
    elif 35 <= result < 40:
        conclusion = f'Ожирение II ст. (ИМТ = {result}{units}).'
    elif result >= 40:
        conclusion = f'Ожирение III ст. (ИМТ = {result}{units}).'

    # предложение добавить в диагноз ожирение
    if result >= 30:
        questionDS = True

    return result, units, conclusion, questionDS


def prepare_data_mrc_ash(d, time_line, i=None):
    '''

    '''
    if time_line == 'первичный':
        x = ''
    elif time_line == 'выписка':
        x = '_вып'
    elif time_line == f'динамика_{i}':
        x = f'_{i}'

    # Создаем список значений шкал,
    # где первый (0) вложенный список это MRC,
    # второй (1) вложенный список это Ashwort,
    st = [[d[f'MRC_R_A_P{x}'],  # Индекс 0
           d[f'MRC_R_A_D{x}'],
           d[f'MRC_R_L_P{x}'],
           d[f'MRC_R_L_D{x}'],
           d[f'MRC_L_A_P{x}'],
           d[f'MRC_L_A_D{x}'],
           d[f'MRC_L_L_P{x}'],
           d[f'MRC_L_L_D{x}']],
          [d[f'Ash_R_A_P{x}'],  # Индекс 1
           d[f'Ash_R_A_D{x}'],
           d[f'Ash_R_L_P{x}'],
           d[f'Ash_R_L_D{x}'],
           d[f'Ash_L_A_P{x}'],
           d[f'Ash_L_A_D{x}'],
           d[f'Ash_L_L_P{x}'],
           d[f'Ash_L_L_D{x}']]]
    for j in range(8):
        if len(st[0][j]) == 1:
            st[0][j] = int(st[0][j])
        else:  # Изменяем промежуточные значения MRC
            if st[0][j] == '0-1':
                st[0][j] = 0.5
            elif st[0][j] == '1-2':
                st[0][j] = 1.5
            elif st[0][j] == '2-3':
                st[0][j] = 2.5
            elif st[0][j] == '3-4':
                st[0][j] = 3.5
            elif st[0][j] == '4-5':
                st[0][j] = 4.5
        if len(st[1][j]) == 1:
            st[1][j] = int(st[1][j])
        else:  # Изменяем промежуточные значения Ashwort
            st[1][j] = 1.5

    return st


def prepare_data_icf(d, time_line, i=None):
    '''

    '''
    if time_line == 'первичный':
        x = ''
    elif time_line == 'выписка':
        x = '_вып'
    elif time_line == f'динамика_{i}':
        x = f'_{i}'
    # Создаем список значений шкал,
    # где первый (0) вложенный список это MRC,
    # второй (1) вложенный список это Ashwort,
    st = [prepare_data_mrc_ash(d, time_line, i),
          d[f'ШРМ{x}'],
          d[f'mRs{x}'],
          d[f'IMR{x}'],
          d[f'хаузер{x}'],
          d[f'ВАШ{x}'],
          d['Правша']]

    return st


# Определение степени выраженности пареза
def severity_of_paresis(st):
    icf_strength = estimate_strength_domen(st)
    if icf_strength in {'0', '1'}:
        return 'легко'
    elif icf_strength in {'2'}:
        return 'умеренно'
    elif icf_strength in {'3'}:
        return 'выраженно'
    elif icf_strength in {'4'}:
        return 'грубо'


# Функция определения наличия пареза
def is_there_paresis(d):

    check = []

    for i in range(1, 3):

        if i == 1:
            st = prepare_data_icf(d, 'первичный')
        elif i == 2:
            st = prepare_data_icf(d, 'выписка')

        right_checking = 0
        left_checking = 0
        right_arm_checking = 0
        right_leg_checking = 0
        left_arm_checking = 0
        left_leg_checking = 0

        for i in range(8):
            if st[0][i] != 5:
                if 0 <= i < 4:
                    right_checking += 1
                    if i == 0 or i == 1:
                        right_arm_checking += 1
                    else:
                        right_leg_checking += 1
                else:
                    left_checking += 1
                    if i == 4 or i == 5:
                        left_arm_checking += 1
                    else:
                        left_leg_checking += 1

        if right_checking == left_checking == 0:
            check.append(False)
        else:
            check.append(True)

    if check[0]:
        if check[1]:
            return True
        else:
            return False
    else:
        return False


# Фукция для интерпретации значения суммарной силы
def interpretation_mrc_assessment(summary, max_mrc):
    if 0 <= 100 - (summary * 100 / max_mrc) < 5:
        return '0'
    elif 5 <= 100 - (summary * 100 / max_mrc) < 25:
        return '1'
    elif 25 <= 100 - (summary * 100 / max_mrc) < 50:
        return '2'
    elif 50 <= 100 - (summary * 100 / max_mrc) < 95:
        return '3'
    elif 95 <= 100 - (summary * 100 / max_mrc) <= 100:
        return '4'
    else:
        print(summary)
        print(max_mrc)
        print(100 - (summary * 100 / max_mrc))
        return 'Что-то пошло не так'


# Функция определения типа пареза (тетра-, геми-, пара-, моно-)
def what_paresis(patient_status):
    right_checking = 0
    left_checking = 0
    right_arm_checking = 0
    right_leg_checking = 0
    left_arm_checking = 0
    left_leg_checking = 0

    for i in range(8):
        if patient_status[0][i] != 5:
            if 0 <= i < 4:
                right_checking += 1
                if i == 0 or i == 1:
                    right_arm_checking += 1
                else:
                    right_leg_checking += 1
            else:
                left_checking += 1
                if i == 4 or i == 5:
                    left_arm_checking += 1
                else:
                    left_leg_checking += 1

    if right_checking == left_checking == 0:
        return 'No paresis'
    elif right_checking > left_checking and left_checking == 0:
        if right_arm_checking != 0 and right_leg_checking != 0:
            return 'Hemiparesis R'
        elif right_arm_checking != 0 and right_leg_checking == 0:
            return 'Monoparesis R superior'
        else:
            return 'Monoparesis R inferior'
    elif left_checking > right_checking and right_checking == 0:
        if left_arm_checking != 0 and left_leg_checking != 0:
            return 'Hemiparesis L'
        elif left_arm_checking != 0 and left_leg_checking == 0:
            return 'Monoparesis L superior'
        else:
            return 'Monoparesis L inferior'
    elif right_checking != 0 and left_checking != 0:
        if right_arm_checking == left_arm_checking == 0:
            return 'Paraparesis inferior'
        elif right_leg_checking == left_leg_checking == 0:
            return 'Paraparesis superior'
        else:
            return 'Tetraparesis'
    else:
        return 'Что-то пошло не так'


# Оценка силы (b730)
def estimate_strength_domen(patient_status):
    paresis = what_paresis(patient_status)
    summary = 0
    max_mrc = 1

    if paresis in ('Hemiparesis R', 'Hemiparesis L'):
        max_mrc = 20
    elif paresis in ('Paraparesis superior', 'Paraparesis inferior'):
        max_mrc = 20
    elif paresis in ('Monoparesis R superior', 'Monoparesis L superior'):
        max_mrc = 10
    elif paresis in ('Monoparesis R inferior', 'Monoparesis L inferior'):
        max_mrc = 10
    elif paresis == 'Tetraparesis':
        max_mrc = 40
    elif paresis == 'No paresis':
        max_mrc = 1

    if paresis == 'No paresis':
        return '0'
    elif paresis == 'Hemiparesis R':
        for i in range(4):
            summary += patient_status[0][i]
    elif paresis == 'Hemiparesis L':
        for i in range(4, 8):
            summary += patient_status[0][i]
    elif paresis == 'Tetraparesis':
        for i in range(0, 8):
            summary += patient_status[0][i]
    elif paresis == 'Paraparesis superior':
        summary = patient_status[0][0] + patient_status[0][1] + \
            patient_status[0][4] + patient_status[0][5]
    elif paresis == 'Paraparesis inferior':
        summary = patient_status[0][2] + patient_status[0][3] + \
            patient_status[0][6] + patient_status[0][7]
    elif paresis == 'Monoparesis R superior':
        summary = patient_status[0][0] + patient_status[0][1]
    elif paresis == 'Monoparesis L superior':
        summary = patient_status[0][4] + patient_status[0][5]
    elif paresis == 'Monoparesis R inferior':
        summary = patient_status[0][2] + patient_status[0][3]
    elif paresis == 'Monoparesis L inferior':
        summary = patient_status[0][6] + patient_status[0][7]

    return interpretation_mrc_assessment(summary, max_mrc)


def get_value_between_brackets(string):
    '''
    '''
    value = ''
    i = 0
    j = 1
    try:
        while string[i] != '(':
            i += 1
        else:
            while string[-j] != ')':
                j += 1
            else:
                value = string[i + 1:-j]
    except IndexError as error:
        print(error)
    finally:
        return value
