'''
В файле config.py располагаются
изменяемые значения для
необходимой настройки скрипта
'''
# значения для диапазона артериального давления (шаг 5)
blood_presure_sist_min = 110
blood_presure_sist_max = 135
blood_presure_diast_min = 70
blood_presure_diast_max = 90

# значения для диапазона ЧСС (шаг 2)
heart_rate_min = 60
heart_rate_max = 80

# значения для диапазона ЧДД (шаг 1)
breath_rate_min = 16
breath_rate_max = 19

# значения для диапазона температуры (шаг 1)
# в генераторе '36,' + str(value)
# т.е. по умолчанию от 36,3 до 36,8
body_temperature_min = 3
body_temperature_max = 8

# значения для диапазона сатурации (шаг 1)
saturation_min = 98
saturation_max = 99

# коэфициент для определения типа дневника на таймлайне
# т.е. после какого процента пройденного тайлайна,
# меняем дневники на следующую генерацию
frontier = 40  # от 0 до 100

# коэфициент на таймлайне для определения ВАШ в дневнике наблюдение
frontier_VAS_1 = 25  # от 0 до 100
frontier_VAS_2 = 70  # от 0 до 100

# словарь для создания полного имени врача
doc_dict = {
    'Тыричев С.В.': (
        'Тыричев Сергей Васильевич', '3513'
    ),
    'Тимофеев А.П.': (
        'Тимофеев Андрей Петрович', ''
    ),
    'Шилов И.С.': (
        'Шилов Илья Сергеевич', ''
    ),
}

doc_dict_bta = {
    'Тимофеев А.П.': (
        'Тимофеев Андрей Петрович', ''
    ),
    'Шилов И.С.': (
        'Шилов Илья Сергеевич', ''
    ),
}

head_department = [
    'Тыричев С.В.',
]
for doc in doc_dict:
    head_department.append(f"И.О.З.О. {doc}")


head_department_bta = [
    'Быстрова О.В.',
    'И.О.З.О. Зайцева Н.В.',
]

# списки Членов МДРК
mdrk_members = {
    'lfk': [
        'Фамилия И.О.',
    ],
    'psy': [
        'Фамилия И.О.',
    ],
    'logo': [
        'Фамилия И.О.',
    ],
    'physio': [
        'Фамилия И.О.',
    ]
}

bed_profiles = [
    'реабилитационные для больных с заболеваниями центральной нервной системы и органов чувств',  # noqa: E501
    'реабилитационные для больных с заболеваниями опорно-двигательного аппарата и периферической нервной системы',  # noqa: E501
    'реабилитационные соматические для взрослых',
]

rooms = [
    '',
    '501',
    '502',
    '503',
    '504',
    '505',
    '506',
    '507',
    '508',
    '509',
    '510',
    '601',
    '602',
    '603',
    '604',
    '605',
    '606',
    '607',
    '608',
    '609',
    '610',
]