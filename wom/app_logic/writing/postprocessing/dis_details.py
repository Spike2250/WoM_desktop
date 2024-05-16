from datetime import timedelta
from wom.app_logic.writing.postprocessing.passport import update_doctor_data
from wom.app_logic.service_func import datedif, convert_date as c_date


def update_after_dis_details(d):
    '''
    '''
    update_doctor_data(d)

    # добавляем койко-дни
    day_dis = d['дата_выписки']
    day_adm = d['дата_поступления']
    typeHosp = d['тип_стационара']
    if typeHosp in {'Круглосуточный стационар', 'БТ - круглосуточный'}:
        d['койкодни'] = datedif(day_adm, day_dis) - 1
    else:
        d['койкодни'] = datedif(day_adm, day_dis)

    # добавляем дату приема в поликлинике
    if (x := int((dis_date := c_date(d['дата_выписки'])).strftime('%w'))) == 5:
        d['дата_прием'] = (dis_date + timedelta(3)).strftime('%d.%m.%Y')
    elif x == 6:
        d['дата_прием'] = (dis_date + timedelta(2)).strftime('%d.%m.%Y')
    elif x in (0, 1, 2, 3, 4):
        d['дата_прием'] = (dis_date + timedelta(1)).strftime('%d.%m.%Y')
