
from wom.app_logic.handbooks\
    .icf_full import (icf_qualifier_degree as ICF_DEGREE,
                      icf_qualifier_structure as ICF_STRUCT,
                      icf_qualifier_localization as ICF_LOCAL,
                      icf_activity_degree as ICF_ACT_DEGREE,
                      icf_environment_relief as ICF_RELIEF,
                      icf_environment_barrier as ICF_BARRIER)


def update_after_icf(d, type_icf):
    if type_icf == 'frm':
        icf_types = ['frm', 'psy', 'logo']
        icf_all = []
        for type_ in icf_types:
            for elem in d.get(f'icf_{type_}', []):
                icf_all.append(elem)
        d['icf_all'] = icf_all
        write_icf(d, 'all')
        # psy, logo
    else:
        write_icf(d, type_icf)


def write_icf(d, type_icf):
    # сортируем список доменов
    data = sorted(
        d[f'icf_{type_icf}'],
        key=lambda x: x['domen'],
        reverse=False
    )
    # создаем строки для записи обработынных доменов
    adm_icf = ''
    dis_icf = ''
    # перебираем домены
    for elem in data:
        domen_num, domen_text = elem['domen'].split(' - ')
        adm_num = elem['numbers_adm']
        dis_num = elem['numbers_dis']

        # для доменов структуры
        if domen_num[0] == 's':

            text1 = f"{domen_num}.{adm_num} | {domen_text}\n"\
                    f"\tВыраженность нарушения: "\
                    f"({adm_num[0]}) - {ICF_DEGREE[adm_num[0]]}\n"\
                    f"\tХарактер нарушения: "\
                    f"({adm_num[1]}) - {ICF_STRUCT[adm_num[1]]}\n"\
                    f"\tЛокализация нарушения: "\
                    f"({adm_num[2]}) - {ICF_LOCAL[adm_num[2]]}\n"

            text2 = f"{domen_num}.{dis_num} | {domen_text}\n"\
                    f"\tВыраженность нарушения: "\
                    f"({dis_num[0]}) - {ICF_DEGREE[dis_num[0]]}\n"\
                    f"\tХарактер нарушения: "\
                    f"({dis_num[1]}) - {ICF_STRUCT[dis_num[1]]}\n"\
                    f"\tЛокализация нарушения: "\
                    f"({dis_num[2]}) - {ICF_LOCAL[dis_num[2]]}\n"

            adm_icf += text1
            dis_icf += text2

        # для доменов функций
        elif domen_num[0] == 'b':

            text1 = f"{domen_num}.{adm_num} | {domen_text}"\
                    f"    ({adm_num[0]}) - {ICF_DEGREE[adm_num[0]]}\n"

            text2 = f"{domen_num}.{dis_num} | {domen_text}"\
                    f"    ({dis_num[0]}) - {ICF_DEGREE[dis_num[0]]}\n"

            adm_icf += text1
            dis_icf += text2

        # для доменов активности и участия
        elif domen_num[0] == 'd':

            text1 = f"{domen_num}.{adm_num} | {domen_text}\n"
            text2 = f"{domen_num}.{dis_num} | {domen_text}\n"

            for i in range(len(adm_num)):
                if i == 0:
                    text = '\tРеализация: '
                elif i == 1:
                    text = '\tКапаситет: '
                elif i == 2:
                    text = '\tКапаситет с посторонней помощью: '
                elif i == 3:
                    text = '\tРеализация без посторонней помощи: '
                adm_s = f"{text}({adm_num[i]})"\
                        f" - {ICF_ACT_DEGREE[adm_num[i]]}\n"
                text1 += adm_s

            # второй цикл нужен для того,
            # чтоб при разном количестве определителей,
            # при поступлении и при выписке, не было ошибки
            for i in range(len(dis_num)):
                if i == 0:
                    text = '\tРеализация: '
                elif i == 1:
                    text = '\tКапаситет: '
                elif i == 2:
                    text = '\tКапаситет с посторонней помощью: '
                elif i == 3:
                    text = '\tРеализация без посторонней помощи: '
                dis_s = f"{text}({dis_num[i]})"\
                        f" - {ICF_ACT_DEGREE[dis_num[i]]}\n"
                text2 += dis_s

            adm_icf += text1
            dis_icf += text2

        # для доменов окружающей среды
        elif domen_num[0] == 'e':

            text1 = f"{domen_num}.{adm_num} | {domen_text}\n"
            text2 = f"{domen_num}.{dis_num} | {domen_text}\n"

            if adm_num[0] == '+':
                adm_s = f"\tОблегчающие факторы: "\
                        f"({adm_num[1]})"\
                        f" - {ICF_RELIEF[adm_num[1]]}\n"
                text1 += adm_s
            else:
                adm_s = f"\tБарьеры: "\
                        f"({adm_num[0]})"\
                        f" - {ICF_BARRIER[adm_num[0]]}\n"
                text1 += adm_s

            if dis_num[0] == '+':
                dis_s = f"\tОблегчающие факторы: "\
                        f"({dis_num[1]})"\
                        f" - {ICF_RELIEF[dis_num[1]]}\n"
                text2 += dis_s
            else:
                dis_s = f"\tБарьеры: "\
                        f"({dis_num[0]})"\
                        f" - {ICF_BARRIER[dis_num[0]]}\n"
                text2 += dis_s

            adm_icf += text1
            dis_icf += text2

    text = 'РЕАБИЛИТАЦИОННЫЙ ДИАГНОЗ (по МКФ)\n'
    d[f'icf_{type_icf}_text_adm'] = f"{text}{adm_icf}"
    d[f'icf_{type_icf}_text_dis'] = f"{text}{dis_icf}"
    d[f'icf_{type_icf}_text_adm_no_header'] = f"{adm_icf}"
    d[f'icf_{type_icf}_text_dis_no_header'] = f"{dis_icf}"
