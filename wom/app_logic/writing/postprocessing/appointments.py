from prettytable import PrettyTable
from wom.app_logic.writing.diaries.gen import create_list_days
from wom.settings.appointment_lists import lfk
from wom.app_logic.service_func import convert_date as c_date
from datetime import datetime, timedelta


def update_after_appointments(d):
    update_after_drugs_appointments(d)
    add_dates_list(d)
    update_after_lfk_appointments(d)
    update_after_physio_appointments(d)


def update_after_drugs_appointments(d):
    '''ПЕРЕДЕЛАТЬ
    '''

    end_string_1 = ''
    for i in range(12):
        end_string_1 += '-'
    end_string_2 = '----------------------------------#'\
                   '-----------------------------------'
    end_list = [end_string_1,
                end_string_1,
                end_string_2]

    # Для инъекционного лн
    sol_table = PrettyTable()
    fields = ["Дата назнач.",
              "Дата отмены",
              "Название препарата, доза, режим дозирования, способ введения"]
    sol_table.field_names = fields

    sol_summary = ''
    sol_row_check = 0

    if len(d['d_sol']) > 0:
        for sol in d['d_sol']:
            sol_i = f"{sol['drug']} {sol['dose']} {sol['DS']}; "
            sol_short = f"{sol['drug']} {sol['dose']}"
            sol_summary += sol_i
            sol_i = sol_i[:-2]
            if len(sol_i) <= 70:
                sol_table.add_rows([[sol['date'], '', sol_i],
                                    end_list, ])
                sol_row_check += 2
            else:
                sol_table.add_rows([[sol['date'], '', sol_short],
                                    ['', '', f"{sol['DS']}"],
                                    end_list, ])
                sol_row_check += 3

    d['лечение_инъекции'] = sol_summary
    while sol_row_check < 15:  # Максимальное количество строк Sol
        sol_row_check += 1
        sol_table.add_row(['', '', ''])
    d['назначение_инъекции'] = f"Парентеральные лекарственные формы:\n"\
                               f"{str(sol_table)}"

    # для энтерального лн
    peros_table = PrettyTable()
    peros_table.field_names = fields
    peros_summary = ''
    peros_row_check = 0

    if len(d['d_tab']) > 0:
        for tab in d['d_tab']:
            tab_i = f"{tab['drug']} {tab['dose']} {tab['DS']}; "
            tab_short = f"{tab['drug']} {tab['dose']}"
            peros_summary += tab_i
            tab_i = tab_i[:-2]
            if len(tab_i) <= 70:
                peros_table.add_rows([[tab['date'], '', tab_i],
                                      end_list, ])
                peros_row_check += 2
            else:
                peros_table.add_rows([[tab['date'], '', tab_short],
                                      ['', '', f"{tab['DS']}"],
                                      end_list, ])
                peros_row_check += 3

    d['лечение_таблетки'] = peros_summary
    while peros_row_check < 43:  # Максимальное количество строк peros
        peros_row_check += 1
        peros_table.add_row(['', '', ''])
    d['назначение_таблетки'] = f"Таблетированные и другие энтеральные "\
                               f"лекарственные формы:\n{str(peros_table)}"
    d['назначение_все'] = f"{d['назначение_инъекции']}\n\n"\
                          f"{d['назначение_таблетки']}"


def add_dates_list(d):
    date2 = (c_date(d['дата_выписки']) + timedelta(9)).strftime("%d.%m.%Y")
    dates, dates_datetime = create_list_days(
        d['дата_поступления'], date2)
    d['approx_dates'] = dates
    d['empty_rows'] = ['' for _ in range(8)]
    d['empty_cols'] = ['' for _ in range(len(dates))]


def update_after_lfk_appointments(d):
    lfk_summary = ''
    for app in d['d_lfk']:
        lfk = f"{app['procedure']} " \
              f"{app['regimen']}; "
        lfk_summary += lfk
    d['лфк'] = lfk_summary


def update_after_physio_appointments(d):
    physio_summary = ''
    for app in d['d_physio']:
        physio = f"{app['procedure']} " \
                 f"{app['place']} " \
                 f"{app['regimen']}; "
        physio_summary += physio
    d['физиотерапия'] = physio_summary


def create_lfk_report_sheet(d):
    table = PrettyTable()

    dates, dates_datetime = create_list_days(
        d['дата_поступления'], d['дата_выписки'])

    fields = ['Назначения'] + dates + ['итого, мин']
    table.field_names = fields

    for app in d['d_lfk']:
        name = f"{app['procedure']}, " \
               f"Ед.{app['ed']}"

        pluses = []
        plus_counter = 0
        for i in range(len(dates)):
            week_day = int(dates_datetime[i].strftime("%w"))
            # день поступления или воскресенье
            if i == 0 or week_day == 0:
                pluses.append('')
            # суббота и процедуры нет по субботам
            elif week_day == 6 and \
                    not lfk['procedure'].get(app['procedure'], False):
                pluses.append('')
            # рабочие дни и процедуры в субботу
            else:
                pluses.append('+')
                plus_counter += 1

        try:
            # из строки единиц типа '1,5' делаем 15
            k = int(app['ed'][0] + app['ed'][-1])
            # суммарное время занятий
            sum_ed = str(k * plus_counter)
        except Exception:
            sum_ed = ''

        row = [name] + pluses + [sum_ed]
        table.add_row(row)

    # пустые строки
    for _ in range(12):
        dotted = ['-----' for _ in range(len(dates))]
        long_dotted = ''.join(['-' for _ in range(34)])
        dotted_line = [long_dotted] + dotted + ['----------']
        table.add_row(dotted_line)
        for _ in range(3):
            empties = ['' for _ in range(len(dates) + 2)]
            table.add_row(empties)

    d['lfk_report_sheet'] = str(table)
