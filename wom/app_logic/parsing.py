
def parse_promed(string):
    '''
    функция принимает на вход стандартную (для промеда) строку
    с данными пациента (ФИО, день рождения, номер паспорта и т.д.)

    Стандартный вид строки из промеда:
    "ФИО: XXX XXX XXX Д/р: xx.xx.xxxx Пол: xxxxx    (всегда лишние 4 пробела)
     Соц. статус: Работающий (включая раб. пенсионеров) СНИЛС: xxx-xxx-xxx-xx
     Регистрация: xxxxxxxxxxxxxxxxxxxxxxxx
     Проживает: xxxxxxxxxxxxxxxxxxxxxxx
     Телефон: XXXXXXXXXX
     ИНН:
     Полис: xxxxxxxxxxxxxxxxxx
     Документ: xxxxxxxxxxxxxxxxxxx
     Семейное положение:
     Работа: Должность:"

    на выходе получаем каждое значение отдельно
    записанные в словарь по ключам:
    * surname
    * name
    * dadname
    * birthday
    * sex
    * snils
    * adress
    * phone_number
    * oms_polis
    * passport

    '''
    # разделяем большую строку по строкам
    list_of_strings = string.split('\n')

    # пробегаемся циклом по каждой строке
    for i in range(len(list_of_strings)):
        if i == 0:  # первая строка
            words = list_of_strings[i].split(' ')
            surname = words[1].lower().capitalize()
            name = words[2].lower().capitalize()
            dadname = words[3].lower().capitalize()
            birthday = words[-7]  # из-за 4 пробелов в конце строки
            sex = words[-5]  # из-за 4 пробелов в конце строки
        elif i == 1:  # вторая строка
            words = list_of_strings[i].split(' ')
            snils = words[-1]
        elif i == 3:  # четвертая строка
            adress = list_of_strings[i][13:]
        elif i == 5:  # шестая строка
            words = list_of_strings[i].split(' ')
            if len(words) > 1:
                phone_number = words[1]
                if len(phone_number) < 11:
                    phone_number = '8' + phone_number
            else:
                phone_number = ''
        elif i == 7:  # седьмая строка
            oms_polis = list_of_strings[i][7:-8]
        elif i == 8:  # восьмая строка
            passport = list_of_strings[i][10:]

    # записываем полученные данные в словарь
    data = {'surname': surname,
            'name': name,
            'dadname': dadname,
            'birthday': birthday,
            'sex': sex,
            'snils': snils,
            'adress': adress,
            'phone_number': phone_number,
            'oms_polis': oms_polis,
            'passport': passport}

    return data
