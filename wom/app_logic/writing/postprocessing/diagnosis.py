from wom.app_logic.service_func import prepare_data_mrc_ash, what_paresis


def update_scale(d, time_line, i=None):
    '''
    '''
    if time_line == 'первичный':
        x = ''
    elif time_line == 'выписка':
        x = '_вып'
    elif time_line == f'динамика_{i}':
        x = f'_{i}'

    st = prepare_data_mrc_ash(d, time_line, i)
    type_paresis = what_paresis(st)

    # определители
    dext = 'Hemiparesis R', 'Monoparesis R superior', 'Monoparesis R inferior'
    sntr = 'Hemiparesis L', 'Monoparesis L superior', 'Monoparesis L inferior'
    no_paresis = 'No paresis'
    tetra = 'Tetraparesis'
    para_sup = 'Paraparesis superior'
    para_inf = 'Paraparesis inferior'

    mrc_ash = ''

    if type_paresis in dext:  # для правосторонних парезов
        mrc_ash = f"MRC: Справа: в/конечность проксимально " \
                  f"{d[f'MRC_R_A_P{x}']}б, дистально {d[f'MRC_R_A_D{x}']}б\n" \
                  f"\t\tн/конечность проксимально {d[f'MRC_R_L_P{x}']}б, " \
                  f"дистально {d[f'MRC_R_L_D{x}']}б\n" \
                  f"\tСлева: 5б во всех группах мышц\n" \
                  f"Ashwort: Справа: в/конечность проксимально " \
                  f"{d[f'Ash_R_A_P{x}']}б, дистально {d[f'Ash_R_A_D{x}']}б\n" \
                  f"\t\tн/конечность проксимально {d[f'Ash_R_L_P{x}']}б, " \
                  f"дистально {d[f'Ash_R_L_D{x}']}б\n" \
                  f"\tСлева: 0б во всех группах мышц"

    elif type_paresis in sntr:  # для левосторонних парезов
        mrc_ash = f"MRC: Слева: в/конечность проксимально " \
                  f"{d[f'MRC_L_A_P{x}']}б, дистально {d[f'MRC_L_A_D{x}']}б\n" \
                  f"\t\tн/конечность проксимально {d[f'MRC_L_L_P{x}']}б, " \
                  f"дистально {d[f'MRC_L_L_D{x}']}б\n" \
                  f"\tСправа: 5б во всех группах мышц\n" \
                  f"Ashwort: Слева: в/конечность проксимально " \
                  f"{d[f'Ash_L_A_P{x}']}б, дистально {d[f'Ash_L_A_D{x}']}б\n" \
                  f"\t\tн/конечность проксимально {d[f'Ash_L_L_P{x}']}б, " \
                  f"дистально {d[f'Ash_L_L_D{x}']}б\n" \
                  f"\tСправа: 0б во всех группах мышц"

    elif type_paresis == tetra:  # для тетпапареза
        mrc_ash = f"MRC: Справа: в/конечность проксимально " \
                  f"{d[f'MRC_R_A_P{x}']}б, дистально {d[f'MRC_R_A_D{x}']}б\n" \
                  f"\t\tн/конечность проксимально {d[f'MRC_R_L_P{x}']}б, " \
                  f"дистально {d[f'MRC_R_L_D{x}']}б\n" \
                  f"\tСлева:  в/конечность проксимально " \
                  f"{d[f'MRC_L_A_P{x}']}б, дистально {d[f'MRC_L_A_D{x}']}б\n" \
                  f"\t\tн/конечность проксимально {d[f'MRC_L_L_P{x}']}б, " \
                  f"дистально {d[f'MRC_L_L_D{x}']}б\n" \
                  f"Ashwort: Справа: в/конечность проксимально " \
                  f"{d[f'Ash_R_A_P{x}']}б, дистально {d[f'Ash_R_A_D{x}']}б\n" \
                  f"\t\tн/конечность проксимально {d[f'Ash_R_L_P{x}']}б, " \
                  f"дистально {d[f'Ash_R_L_D{x}']}б\n" \
                  f"\tСлева:  в/конечность проксимально " \
                  f"{d[f'Ash_L_A_P{x}']}б, дистально {d[f'Ash_L_A_D{x}']}б\n" \
                  f"\t\tн/конечность проксимально {d[f'Ash_L_L_P{x}']}б, " \
                  f"дистально {d[f'Ash_L_L_D{x}']}б"

    elif type_paresis == no_paresis:  # если пареза нет
        mrc_ash = f'MRC: Справа и слева - 5б во всех мышечных группах\n' \
                  f'Ashwort: Справа и слева - 0б во всех мышечных группах'

    elif type_paresis == para_sup:  # для верхнего парапареза
        mrc_ash = f"MRC: В/конечность: Справа: проксимально " \
                  f"{d[f'MRC_R_A_P{x}']}б, дистально {d[f'MRC_R_A_D{x}']}б\n" \
                  f"\t\t\tСлева:  проксимально {d[f'MRC_L_A_P{x}']}б, " \
                  f"дистально {d[f'MRC_L_A_D{x}']}б\n" \
                  f"\tН/конечность - Справа и слева 5б " \
                  f"во всех мышечных группах\n" \
                  f"Ashwort: В/конечность: Справа: проксимально " \
                  f"{d[f'Ash_R_A_P{x}']}б, дистально {d[f'Ash_R_A_D{x}']}б\n" \
                  f"\t\tСлева:  проксимально {d[f'Ash_L_A_P{x}']}б, " \
                  f"дистально {d[f'Ash_L_A_D{x}']}б\n" \
                  f"\tН/конечность - Справа и слева 0б " \
                  f"во всех мышечных группах"

    elif type_paresis == para_inf:  # для нижнего парапареза
        mrc_ash = f"MRC: Н/конечность: Справа: проксимально " \
                  f"{d[f'MRC_R_L_P{x}']}б, дистально {d[f'MRC_R_L_D{x}']}б\n" \
                  f"\t\t\tСлева:  проксимально {d[f'MRC_L_L_P{x}']}б, " \
                  f"дистально {d[f'MRC_L_L_D{x}']}б\n" \
                  f"\tВ/конечность - Справа и слева 5б " \
                  f"во всех мышечных группах\n" \
                  f"Ashwort: Н/конечность: Справа: проксимально " \
                  f"{d[f'Ash_R_L_P{x}']}б, дистально {d[f'Ash_R_L_D{x}']}б\n" \
                  f"\t\t\tСлева:  проксимально {d[f'Ash_L_L_P{x}']}б, " \
                  f"дистально {d[f'Ash_L_L_D{x}']}б\n" \
                  f"\tВ/конечность - Справа и слева 0б " \
                  f"во всех мышечных группах"

    if d['наличие_боли']:
        func_scale = f"Шкала Рэнкин {d[f'mRs{x}']}. " \
                     f"ШРМ {d[f'ШРМ{x}']}. " \
                     f"Индекс Ривермид {d[f'IMR{x}']}. " \
                     f"Ходьба по Хаузеру {d[f'хаузер{x}']}. " \
                     f"ВАШ {d[f'VAS{x}']}."
        # d['ВАШ_список'] = create_VPS_table(d)

    else:
        func_scale = f"Шкала Рэнкин {d[f'mRs{x}']}. " \
                     f"ШРМ {d[f'ШРМ{x}']}. " \
                     f"Индекс Ривермид {d[f'IMR{x}']}. " \
                     f"Ходьба по Хаузеру {d[f'хаузер{x}']}."

    scale_text = f"{func_scale}\n" \
                 f"{mrc_ash}"

    d[f'Шкалы{x}'] = scale_text


def update_after_diagnosis(d):
    '''
    '''
    if 'MRC_R_A_D' in d:
        update_scale(d, 'первичный')
    if 'MRC_R_A_D_вып' in d:
        update_scale(d, 'выписка')
