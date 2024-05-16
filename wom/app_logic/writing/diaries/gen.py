from random import choice
from datetime import timedelta
from ast import literal_eval
from wom.settings.config import (blood_presure_sist_min,
                                 blood_presure_sist_max,
                                 blood_presure_diast_min,
                                 blood_presure_diast_max,
                                 heart_rate_min,
                                 heart_rate_max,
                                 breath_rate_min,
                                 breath_rate_max,
                                 body_temperature_min,
                                 body_temperature_max,
                                 saturation_min,
                                 saturation_max,
                                 frontier_VAS_1,
                                 frontier_VAS_2,
                                 frontier)
from wom.app_logic.service_func import convert_date
from wom.app_logic.writing.diaries\
    .diary_templates import (tpl_stamp,
                             create_vps_diary)


def create_random_set():
    blood_presure_sist = str(choice(range(
        blood_presure_sist_min,
        blood_presure_sist_max + 1, 5)))
    blood_presure_diast = str(choice(range(
        blood_presure_diast_min,
        blood_presure_diast_max + 1, 5)))
    heart_rate = str(choice(range(
        heart_rate_min,
        heart_rate_max + 1, 2)))
    breath_rate = str(choice(range(
        breath_rate_min,
        breath_rate_max + 1)))
    body_temperature = "36," + str(choice(range(
        body_temperature_min,
        body_temperature_max + 1)))
    saturation = str(choice(range(
        saturation_min,
        saturation_max + 1)))
    return {
        'bp_sist': blood_presure_sist,
        'bp_diast': blood_presure_diast,
        'heart_rate': heart_rate,
        'breath_rate': breath_rate,
        'temperature': body_temperature,
        'saturation': saturation
    }


#  = = = = Создание дневников = = = =
# PS. нужен модуль tpl_gen.py
#
# добавление наборов значений для дневников
def add_random_values(d, n, twice_diaries):
    '''
    Функция добавления к словарю случайных
    наборов данных для АД, ЧСС, ЧДД,
    температуры тела, сатурации,
    времени для дневников

    в количестве 'n'

    * twice_diaries - модификатор для написания
      вечернего времени при написании дневников дважды в день
    '''
    for m in range(1, n + 1):
        random_set = create_random_set()
        d[f"АД_сист_{m}"] = random_set['bp_sist']
        d[f"АД_диаст_{m}"] = random_set['bp_diast']
        d[f"ЧСС_{m}"] = random_set['heart_rate']
        d[f"ЧДД_{m}"] = random_set['breath_rate']
        d[f"Температура_{m}"] = random_set['temperature']
        d[f"Сатурация_{m}"] = random_set['saturation']
        if not twice_diaries:
            d[f'время_доп_{m}'] = f'0{str(choice(range(8, 10)))}:' \
                                  f'{str(choice(range(10, 56, 5)))}'
        else:  # если дневники дважды в день
            if m % 2 == 0:  # если четная итерация - пишем вечернее время
                d[f'время_доп_{m}'] = f'{str(choice(range(17, 20)))}:' \
                                      f'{str(choice(range(10, 56, 5)))}'
            else:
                d[f'время_доп_{m}'] = f'0{str(choice(range(8, 10)))}:' \
                                      f'{str(choice(range(10, 56, 5)))}'
        d[f'знч_днев_{m}'] = f"Температура тела {d[f'Температура_{m}']} С.\t"\
                             f"АД {d[f'АД_сист_{m}']}/{d[f'АД_диаст_{m}']} "\
                             f"мм.рт.ст.\n"\
                             f"ЧДД {d[f'ЧДД_{m}']} в 1 минуту. "\
                             f"SpO2 {d[f'Сатурация_{m}']} %.\t"\
                             f"ЧСС {d[f'ЧСС_{m}']} уд/мин. "


# Cоздание списка дат (будней) от date1 до date2, без date1 в списке.
def create_list_work_days(date1, date2):
    '''
    Функция принимает 2 числа в формате 'дд.мм.гггг'
    date1 дата после которой начинается формироваться список,
                                        НЕ включается в список
    date2 дата до которой список формируется, date2 включается в список

    в цикле формирования списка присутствует проверка дня недели
    субботы и воскресения в список НЕ вносятся (кроме date2)

    Возвращает  ДВА(!) списка дат
    1й в формате дд.мм.гггг
    2й в формате datetime.datetime

    '''
    # конвертируем даты в datetime.datetime
    date1, date2 = convert_date(date1), convert_date(date2)
    delta = date2 - date1  # считаем разницу дат
    # вводим переменную d для цикла,
    # равна разнице целых дней между указанными датами
    d = delta.days
    DateList = []  # создаем пустой список для цикла куда будем вписывать даты
    DateListSimple = []  # -//-
    for i in range(1, d):  # ЦИКЛ [1 ; d)
        # переменная date_next принимает значение даты
        # от (date1 + 1 день) до (date2 - 1 день)
        date_next = date1 + timedelta(i)
        # проверка дня недели
        # если от 1 до 5 (пн до пт), дата вносится в список
        if 0 < int(date_next.strftime("%w")) < 6:
            # вписание значений в список DateList в формате datetime.datetime
            DateList.append(date_next)
            # вписание значений в список DateListSimple в формате дд.мм.гггг
            DateListSimple.append(date_next.strftime("%d.%m.%Y"))

    # вписываем date2
    DateListSimple.append(date2.strftime("%d.%m.%Y"))
    DateList.append(date2)
    # возвращаем созданные списоки, первый в формате дд.мм.гггг
    return DateListSimple, DateList


# Cоздание списка дат (ПН, СР, ПТ) от date1 до date2, без date1 в списке.
def create_list_work_days_135(date1, date2):
    '''
    Функция принимает 2 числа в формате 'дд.мм.гггг'
    date1 дата после которой начинается формироваться список,
                                        НЕ включается в список
    date2 дата до которой список формируется, date2 включается в список

    в цикле формирования списка присутствует проверка дня недели
    субботы и воскресения в список НЕ вносятся (кроме date2)

    Возвращает  ДВА(!) списка дат
    1й в формате дд.мм.гггг
    2й в формате datetime.datetime

    '''
    # конвертируем даты в datetime.datetime
    date1, date2 = convert_date(date1), convert_date(date2)

    delta = date2 - date1  # считаем разницу дат
    # вводим переменную d для цикла,
    # равна разнице целых дней между указанными датами
    d = delta.days
    DateList = []  # создаем пустой список для цикла куда будем вписывать даты
    DateListSimple = []  # -//-
    for i in range(1, d):  # ЦИКЛ [1 ; d)
        # переменная date_next принимает значение даты
        # от (date1 + 1 день) до (date2 - 1 день)
        date_next = date1 + timedelta(i)
        # проверка дня недели
        if int(date_next.strftime("%w")) in {1, 3, 5}:  # ПН, СР, ПТ
            # вписание значений в список DateList в формате datetime.datetimeй
            DateList.append(date_next)
            # вписание значений в список DateListSimple в формате дд.мм.гггг
            DateListSimple.append(date_next.strftime("%d.%m.%Y"))

    # вписываем date2
    DateListSimple.append(date2.strftime("%d.%m.%Y"))
    DateList.append(date2)
    # возвращаем созданные списоки, первый в формате дд.мм.гггг
    return DateListSimple, DateList


# Cоздание списка двойных дат (будней) от date1 до date2, без date1 в списке.
def create_double_list_work_days(date1, date2):
    '''
    Функция принимает 2 числа в формате 'дд.мм.гггг'
    date1 дата после которой начинается формироваться список,
                                        НЕ включается в список
    date2 дата до которой список формируется, date2 включается в список

    в цикле формирования списка присутствует проверка дня недели
    субботы и воскресения в список НЕ вносятся (кроме date2)

    формируются списки с ДВОЙНЫМИ датами

    Возвращает  ДВА(!) списка дат
    1й в формате дд.мм.гггг
    2й в формате datetime.datetime

    '''
    # конвертируем даты в datetime.datetime
    date1, date2 = convert_date(date1), convert_date(date2)
    delta = date2 - date1  # считаем разницу дат
    # вводим переменную d для цикла,
    # равна разнице целых дней между указанными датами
    d = delta.days
    DateList = []  # создаем пустой список для цикла куда будем вписывать даты
    DateListSimple = []  # -//-
    for i in range(1, d):  # ЦИКЛ [1 ; d)
        # переменная date_next принимает значение даты
        # от (date1 + 1 день) до (date2 - 1 день)
        date_next = date1 + timedelta(i)
        # проверка дня недели
        # если от 1 до 5 (пн до пт), дата вносится в список
        if 0 < int(date_next.strftime("%w")) < 6:
            # вписание значений в список DateList в формате datetime.datetime
            DateList.append(date_next)
            DateList.append(date_next)
            # вписание значений в список DateListSimple в формате дд.мм.гггг
            DateListSimple.append(date_next.strftime("%d.%m.%Y"))
            DateListSimple.append(date_next.strftime("%d.%m.%Y"))

    # вписываем date2
    DateListSimple.append(date2.strftime("%d.%m.%Y"))
    DateList.append(date2)
    # возвращаем созданные списоки, первый в формате дд.мм.гггг
    return DateListSimple, DateList


# Cоздание списка дат  от date1 до date2.
def create_list_days(date1, date2):
    '''
    Функция принимает 2 числа в формате 'дд.мм.гггг'
    date1 дата после которой начинается формироваться список,
                                        включается в список
    date2 дата до которой список формируется, date2 включается в список

    Возвращает  ДВА(!) списка дат
    1й в формате дд/мм
    2й в формате datetime.datetime

    '''
    # конвертируем даты в datetime.datetime
    date1, date2 = convert_date(date1), convert_date(date2)
    delta = date2 - date1  # считаем разницу дат
    # вводим переменную d для цикла,
    # равна разнице целых дней между указанными датами
    d = delta.days
    DateList = []  # создаем пустой список для цикла куда будем вписывать даты
    DateListSimple = []  # -//-
    for i in range(d):  # ЦИКЛ [1 ; d)
        # переменная date_next принимает значение даты
        # от (date1 + 1 день) до (date2 - 1 день)
        date_next = date1 + timedelta(i)
        # проверка дня недели

        # вписание значений в список DateList в формате datetime.datetime
        DateList.append(date_next)
        # вписание значений в список DateListSimple в формате дд.мм.гггг
        DateListSimple.append(date_next.strftime("%d/%m"))

    # вписываем date2
    DateListSimple.append(date2.strftime("%d/%m"))
    DateList.append(date2)
    # возвращаем созданные списоки, первый в формате дд.мм.гггг
    return DateListSimple, DateList


# генерирование всех дневниковых
# записей для всех рабочих дней
def creating_diaries(d, mode):
    '''
    Принимает словарь с исходными данными пациента

    по dict['дата_поступления'] и dict['дата_выписки']
    генерирует список рабочих дней (соответственно дней,
    в которые необходимо написать дневник)

    создает дневник для каждого рабочего дня и даты выписки
    и вписывает их в словарь

    возвращает словарь с вписанными в него дневниками по ключам
    dict['дневник_текст_i'], где i номер дневниковой записи

    '''
    # создаем список рабочих дней
    if mode == 'everyday':
        work_days = create_list_work_days(
            d['дата_поступления'],
            d['дата_выписки_план'])
        twice_diaries = False
    elif mode == '3timesWeek':
        work_days = create_list_work_days_135(
            d['дата_поступления'],
            d['дата_выписки_план'])
        twice_diaries = False
    elif mode == 'twice_everyday':
        work_days = create_double_list_work_days(
            d['дата_поступления'],
            d['дата_выписки_план'])
        twice_diaries = True

    week_day_adm = int(convert_date(d['дата_поступления']).strftime("%w"))

    n_day = None

    # если пациент поступил в понедельник или вторник
    if week_day_adm in {1, 2}:
        # МДРК в среду
        n_day = 3
    # если пациент поступил в среду
    elif week_day_adm in {3, 4}:
        # МДРК в пятницу
        n_day = 5
    # если пациент поступил с четверга по воскресенье
    elif week_day_adm in {5, 6, 0}:
        # МДРК в понедельник
        n_day = 1

    # генерируем случайные наборы значений для дневников
    # в количестве равном количеству рабочих дней
    add_random_values(d, len(work_days[0]), twice_diaries)

    full_diary = ''
    table_data = []
    # пробегаемся по созданному списку рабочих дней циклом
    for i in range(1, len(work_days[0]) + 1):
        # присвоение значения соответствующей дате дневника
        d['дата_дневники_' + str(i)] = work_days[0][i - 1]

        # из модуля tpl_gen.py
        create_md_record(d, i, work_days[1][i - 1], n_day, twice_diaries)

        # создание единого текста дневников
        diary = d[f'дневник_текст_{i}']
        diary = diary + '\n'
        full_diary += diary

        if work_days[0][i - 1] == d['дата_выписки']:
            table_data.append((work_days[0][i - 1], 'Итоговый осмотр'))
        elif int(work_days[1][i - 1].strftime("%w")) == n_day:
            if not twice_diaries:
                table_data.append((work_days[0][i - 1], 'МДРК'))
            else:  # если дневники дважды в день
                if i % 2 == 0:  # если итерация четная - дневник
                    table_data.append((work_days[0][i - 1], 'Дневник'))
                else:
                    table_data.append((work_days[0][i - 1], 'МДРК'))
        else:
            table_data.append((work_days[0][i - 1], 'Дневник'))

    d['дневники_табл'] = table_data
    d['дневник_текст_все'] = full_diary[2:]

    # Добавление дневника боли, при ее наличии
    write_vps_table(d)


def write_vps_table(d):
    if d['наличие_боли']:

        d['дневник_текст_все'] += d['ВАШ_список']

        if isinstance(d['дневники_табл'], str):
            # делаем из строки - список кортежей обратно
            d['дневники_табл'] = literal_eval(d['дневники_табл'])
        d['дневники_табл'].append((d['дата_выписки'], 'Динамика ВАШ'))


# формирование строки всего дневника наблюдения ВАШ
def concatenate_VPS_dairy(date_list, vps_list):
    '''
    '''
    vps_diary_table = ''

    for i in range(len(vps_list)):
        vps_diary = f'  {date_list[i]}       -           {vps_list[i]}\n'
        vps_diary_table += vps_diary

    return vps_diary_table


# анализирование необходимости и написание
# дневника наблюдения по ВАШ-боли на все рабочие дни
def create_VPS_table(d):
    '''
    '''
    date_list = create_list_work_days(
        d['дата_поступления'],
        d['дата_выписки'])
    vps_list = []

    for i in range(len(date_list[0])):
        k = check_time_line(  # из tpl_gen.py
            date_list[1][i],
            d['дата_поступления'],
            d['дата_выписки'])

        if k <= frontier_VAS_1:  # из config
            vps_list.append(d['VAS'])
        elif k <= frontier_VAS_2:  # из config
            vps_list.append(f"{int(d['VAS_вып']) + 1}")
        else:
            vps_list.append(d['VAS_вып'])

    vps_diary = create_vps_diary(d,
                                 concatenate_VPS_dairy(
                                     date_list[0],
                                     vps_list))
    return vps_diary


def check_time_line(date, date_from, date_until):
    '''
    Функция для определения места date в таймлайне между date_from и date_unil

    Принимает 3 даты:
    1 - date - дата для которой считаем коэффициент места в таймлайне
                                          (ВАЖНО: в формате datetime.datetime)
    2 - date_from - дата начала таймлайна (ВАЖНО: в формате 'дд.мм.гггг')
    3 - date_until - дата конца таймлайна (ВАЖНО: в формате 'дд.мм.гггг')

    Возвращает коэффициент (от 0.0% до 100.0%) - для определения позиции даты
    в этом таймлайне, где 0% это начало, а 100% - последний день таймлайна

    '''
    # Конвертируем 'дд.мм.гггг' в datetime.datetime
    date_from = convert_date(date_from)
    date_until = convert_date(date_until)

    # считаем разницу дат
    delta_max = date_until - date_from
    delta_check = date - date_from

    # считаем долю в timeline'е для date (в %)
    k = round((delta_check * 100 / delta_max), 1)

    return k  # возвращаем полученный коэффициент


def god_power(d, i, date, k, stamps, n, twice_diaries):
    '''
    d - словарь
    i - номер итерации
    date - дата для которой пишем запись (в datetime.datetime)
    k - коэффициент положения date в таймлайне
    stamps - словарь шаблонов дневников
      с ключами
        ['mdrk_var_1'] - для МДРК в первую половину таймлайна
        ['mdrk_var_2'] - для МДРК во вторую половину таймлайна
        ['diary_var_1'] - для обычного дневника в первую половину таймлайна
        ['diary_var_2'] - для обычного дневника во вторую половину таймлайна
        ['final_diary'] - для итогового осмотра в день выписки
    n - день n (int 1, 3 или 5), день недели в который пишем МДРК\
    twice_diaries - bool, дважды ли в день дневники
    '''
    # если сегодня день n
    if int(date.strftime("%w")) == n:
        if not twice_diaries:
            if k <= frontier:  # первая половина таймлайна
                d[f'дневник_текст_{i}'] = stamps['mdrk_var_1']
            else:  # вторая половина таймлайна
                d[f'дневник_текст_{i}'] = stamps['mdrk_var_2']
        else:
            if i % 2 == 0:  # если итерация четная пишем обычный дневник
                if k <= frontier:  # первая половина таймлайна
                    d[f'дневник_текст_{i}'] = stamps['diary_var_1']
                else:  # вторая половина таймлайна
                    d[f'дневник_текст_{i}'] = stamps['diary_var_2']
            else:  # если итерация нечетная пишем МДРК
                if k <= frontier:  # первая половина таймлайна
                    d[f'дневник_текст_{i}'] = stamps['mdrk_var_1']
                else:  # вторая половина таймлайна
                    d[f'дневник_текст_{i}'] = stamps['mdrk_var_2']

    # если не день n, то пишем простой дневник
    elif int(date.strftime("%w")) != n:
        if k <= frontier:  # первая половина таймлайна
            d[f'дневник_текст_{i}'] = stamps['diary_var_1']
        else:  # вторая половина таймлайна
            d[f'дневник_текст_{i}'] = stamps['diary_var_2']


def create_md_record(d, i, date, n_day, twice_diaries):
    '''
    d - словарь
    i - номер итерации
    date - дата для которой пишем запись (в datetime.datetime)
    '''
    # ОПРЕДЕЛЯЕМ ТИП ДНЕВНИКОВОЙ ЗАПИСИ
    # определяем где на таймлайне госпитализации мы находимся
    k = check_time_line(date, d['дата_поступления'], d['дата_выписки'])
    # создаем словарь со штампами дневников
    stamps = tpl_stamp(d, i)  # из модуля templates

    if k == 100:  # день выписки

        d[f'дневник_текст_{i}'] = stamps['final_diary']
        d['итоговый_осмотр_с_зав_отделением'] = stamps['final_diary']

        return d

    god_power(d, i, date, k, stamps, n_day, twice_diaries)
