'''
'''


def create_vps_diary(d, string):
    '''
    '''
    vps_diary = f"\n\n\t\tГБУЗ ПК ПККГВВ. " \
                f"Отделение медицинской реабилитации.\n" \
                f"\t\tДинамика болевого синдрома." \
                f"\tИстория болезни №{d['номер_истории']}" \
                f"\nФИО: {d['ФИО_пациента']}, " \
                f"{d['дата_рождения']} ({d['возраст']})\n" \
                f"     Дата           Визуальная аналоговая\n" \
                f"                       шкала боли (ВАШ)\n" \
                f"{string}\n" \
                f"{d['дата_выписки']}г.   09:30\n" \
                f"\nВрач-ФРМ:\t" \
                f"__________________ ({d['ФИО_врача']})"

    return vps_diary


def tpl_stamp(d, i):
    '''
    d - словарь с данными
    i - номер итерации

    Возвращает словарь:
    dict_stamps - словарь шаблонов дневников
      с ключами:
        ['mdrk_var_1'] - для МДРК в первую половину таймлайна
        ['mdrk_var_2'] - для МДРК во вторую половину таймлайна
        ['diary_var_1'] - для обычного дневника в первую половину таймлайна
        ['diary_var_2'] - для обычного дневника во вторую половину таймлайна
        ['final_diary'] - для итогового осмотра в день выписки
    '''
    # ОБЩИЕ ШАБЛОНЫ
    date_time = f"{d['дата_дневники_' + str(i)]}г. {d['время_доп_' + str(i)]}."

    complaints = f"Жалобы, на момент осмотра: {d['жалобы']}"

    st_pr_objectivus = f"Соматический статус: "\
                       f"Общее состояние: {d['Общее_состояние']}.\n"\
                       f"{d[f'знч_днев_{i}']}\n"\
                       f"{d['Соматический_статус_для_дневников']}"

    ns_base = "Неврологический статус:"
    st_neurologic_gen_1 = f"{ns_base}\n" \
                          f"{d['Неврологический_статус']}"

    st_neurologic_gen_2 = f"{ns_base}\n" \
                          f"{d['Неврологический_статус_вып']}"

    st_neur_diary_gen_1 = f"{ns_base} "\
                          f"{d['Неврологический_статус_сокращенный']}"

    st_neur_diary_gen_2 = f"{ns_base} "\
                          f"{d['Неврологический_статус_сокращенный_вып']}"

    diag_main_base = "Основной:"
    diag_main_gen_1 = f"{diag_main_base} {d['Основной_диагноз']}"
    # diag_main_gen_2 = f"{diag_main_base} {d['DS_основной_2']}"
    diag_main_final = f"{diag_main_base} {d['Основной_диагноз_вып']}"

    diag_other_base = "Сопутствующий:"
    diag_other = f"{diag_other_base} {d['Сопутствующий_диагноз']}"
    diag_other_final = f"{diag_other_base} {d['Сопутствующий_диагноз_вып']}"

    diag_func_scale_base = "Функциональные шкалы:"
    diag_func_scale_gen_1 = f"{diag_func_scale_base}\n" \
                            f"{d['Шкалы']}"
    # diag_func_scale_gen_2 = f"{diag_func_scale_base}\n" \
    #                         f"{d['Шкалы_2']}"
    diag_func_scale_final = f"{diag_func_scale_base}\n" \
                            f"{d['Шкалы_вып']}"

    rehab_diagnosis_1 = d[f'icf_all_text_adm_no_header']
    rehab_diagnosis_2 = d[f'icf_all_text_dis_no_header']

    dynamic = f"Динамика: {d['динамика_вып']}"

    # # СПЕЦИАЛЬНЫЕ ШАБЛОНЫ
    # Шаблоны обычного дневника
    heading_diary = f"\n\n\t\tГБУЗ ПК ПККГВВ. " \
                    f"Отделение медицинской реабилитации.\n" \
                    f"\t\t{date_time} Осмотр невролога." \
                    f"\tИстория болезни №{d['номер_истории']}"

    ending_diary = f"Врач-ФРМ:\t" \
                   f"__________________ ({d['ФИО_врача']})"

    # Шаблоны для МДРК
    heading_mdrk = f"\n\n\t\tГБУЗ ПК ПККГВВ. " \
                   f"Отделение медицинской реабилитации.\n" \
                   f"\t\t{date_time}\tИстория болезни " \
                   f"№{d['номер_истории']}\n" \
                   f"\t\tКонсультативное заключение мультидисциплинарной " \
                   f"реабилитационной команды (МДРК)."

    physio_conclusion = f"Физиотерапевтическое лечение: {d['физиотерапия']}"

    lfk_conclusion = f"ЛФК: {d['лфк']}"

    if d['закл_логопеда'] != '':
        logo_conclusion = f"Заключение логопеда: {d['закл_логопеда']}.\n"\
                          f"\tШкала Вассермана: {d['ш_вассермана']}"\
                          f"\tШкала Хаус-Браакман: {d['ш_прозопареза']}"\
                          f"\tШкала Дизартрии: {d['ш_дизартрии']}"\
                          f"\tШкала дисфагии по КИМ: {d['ш_дисфагии']}"
        logo_conclusion_2 = f"Заключение логопеда: {d['закл_логопеда']}.\n"\
                            f"\tШкала Вассермана: {d['ш_вассермана_вып']}"\
                            f"\tШкала Хаус-Браакман: {d['ш_прозопареза_вып']}"\
                            f"\tШкала Дизартрии: {d['ш_дизартрии_вып']}"\
                            f"\tШкала дисфагии по КИМ: {d['ш_дисфагии_вып']}"
    if d['закл_психолога'] != '':
        psy_conclusion = f"Заключение клинического психолога: "\
                         f"{d['закл_психолога']}\n"\
                         f"\tMoCA: {d['MoCA']}\tHADS: "\
                         f"тревога {d['HADS_t']} / депрессия {d['HADS_d']}"
        psy_conclusion_2 = f"Заключение клинического психолога: "\
                           f"{d['закл_психолога']}\n"\
                           f"\tMoCA: {d['MoCA_вып']}\tHADS: "\
                           f"тревога {d['HADS_t_вып']} "\
                           f"/ депрессия {d['HADS_d_вып']}"

    rehab_goals = f"Цели реабилитации: {d['цели_реабилитации']}\n\t" \
                  f"Шкала Рэнкин {d['mRs_вып']}. " \
                  f"ШРМ {d['ШРМ_вып']}. " \
                  f"Индекс Ривермид {d['IMR_вып']}. " \
                  f"Ходьба по Хаузеру {d['хаузер_вып']}."
    limit_factor = f"Факторы ограничивающие реабилитацию: " \
                   f"{d['факторы_ограничивающие_реабилитацию']}"
    rehab_potential = f"Реабилитационный потенциал: " \
                      f"{d['реаб_потенциал']}"

    #
    if d['закл_логопеда'] == '' and d['закл_психолога'] == '':
        ending_mdrk = f"\nВрач-ФРМ:\t" \
                      f"__________________ ({d['ФИО_врача']})\n\n" \
                      f"Врач-ЛФК:\t" \
                      f"__________________ ({d['ФИО_ЛФК']})\n\n" \
                      f"Врач-физиотерапевт:\t" \
                      f"__________________ ({d['ФИО_Физиотерапевт']})\n\n" \
                      f"Зав.отделением:\t" \
                      f"__________________ ({d['зав_отделением']})"

    elif d['закл_логопеда'] == '' and d['закл_психолога'] != '':
        ending_mdrk = f"\nВрач-ФРМ:\t" \
                      f"__________________ ({d['ФИО_врача']})\n\n" \
                      f"Врач-ЛФК:\t" \
                      f"__________________ ({d['ФИО_ЛФК']})\n\n" \
                      f"Врач-физиотерапевт:\t" \
                      f"__________________ ({d['ФИО_Физиотерапевт']})\n\n" \
                      f"Клин.психолог:\t" \
                      f"__________________ ({d['ФИО_психолог']})\n\n" \
                      f"Зав.отделением:\t" \
                      f"__________________ ({d['зав_отделением']})"

    elif d['закл_логопеда'] != '' and d['закл_психолога'] != '':
        ending_mdrk = f"\nВрач-ФРМ:" \
                      f"\t__________________ ({d['ФИО_врача']})\n\n" \
                      f"Врач-ЛФК:" \
                      f"\t__________________ ({d['ФИО_ЛФК']})\n\n" \
                      f"Врач-физиотерапевт:" \
                      f"\t__________________ ({d['ФИО_Физиотерапевт']})\n\n" \
                      f"Логопед:" \
                      f"\t__________________ ({d['ФИО_логопед']})\n\n" \
                      f"Клин.психолог:" \
                      f"\t__________________ ({d['ФИО_психолог']})\n\n" \
                      f"Зав.отделением:" \
                      f"\t__________________ ({d['зав_отделением']})"

    # Шаблоны для итогового осмотра с зав.отделением
    heading_final_diary = f"\n\n\t\tГБУЗ ПК ПККГВВ. " \
                          f"Отделение медицинской реабилитации.\n" \
                          f"\t\t{date_time} Итоговый осмотр совместно " \
                          f"с зав.отделением." \
                          f"\tИстория болезни №{d['номер_истории']}"

    ending_phrase = f"Выписывается в плановом порядке, " \
                    f"в удовлетворительном состоянии, с " \
                    f"улучшением, под наблюдение участкового " \
                    f"терапевта. Выписной эпикриз с " \
                    f"рекомендациями выдан на руки."

    ending_final_diary = f"\nВрач-ФРМ:\t" \
                         f"__________________ ({d['ФИО_врача']})\n\n" \
                         f"Зав.отделением:\t" \
                         f"__________________ ({d['зав_отделением']})"

    # КОНСТРУКТОРЫ БЛОКОВ
    # 1    Жалобы и статус
    collect_status_text_gen_1 = f"{complaints}\n\n" \
                                f"{st_pr_objectivus}\n\n" \
                                f"{st_neurologic_gen_1}"

    # 2
    collect_status_text_gen_2 = f"{complaints}\n\n" \
                                f"{st_pr_objectivus}\n\n" \
                                f"{st_neurologic_gen_2}"

    # 1   Диагноз
    diagnosis_complex_1 = f"{diag_main_gen_1}\n" \
                          f"{diag_other}\n" \
                          f"{diag_func_scale_gen_1}"

    # 2
    diagnosis_complex_2 = f"{diag_main_final}\n" \
                          f"{diag_other_final}\n" \
                          f"{diag_func_scale_final}"

    # 3 (итоговый)
    diagnosis_complex_final = f"{diag_main_final}\n" \
                              f"{diag_other_final}\n" \
                              f"{diag_func_scale_final}"

    # СБОРЩИКИ ВСЕЙ ЗАПИСИ
    # сборщики дневников
    # 1            тут \n не нужен
    diary_var_1 = f"{heading_diary}\n" \
                  f"{complaints}\n" \
                  f"{st_pr_objectivus}\n" \
                  f"{st_neur_diary_gen_1}\n" \
                  f"\n" \
                  f"{ending_diary}"

    # 2            тут \n не нужен
    diary_var_2 = f"{heading_diary}\n" \
                  f"{complaints}\n" \
                  f"{st_pr_objectivus}\n" \
                  f"{st_neur_diary_gen_2}\n" \
                  f"\n" \
                  f"{ending_diary}"

    # сборщики МДРК
    if d['закл_логопеда'] == '' and d['закл_психолога'] == '':
        # 1          тут \n не нужен
        mdrk_var_1 = f"{heading_mdrk}\n" \
                     f"\n" \
                     f"{collect_status_text_gen_1}\n" \
                     f"\n" \
                     f"{physio_conclusion}\n" \
                     f"{lfk_conclusion}\n" \
                     f"\n" \
                     f"{limit_factor}\n" \
                     f"\n" \
                     f"{rehab_potential}\n" \
                     f"\n" \
                     f"{rehab_goals}\n" \
                     f"\n" \
                     f"Клинический диагноз:\n" \
                     f"{diagnosis_complex_1}\n" \
                     f"\n" \
                     f"Реабилитационный диагноз (по МКФ):\n" \
                     f"{rehab_diagnosis_1}\n" \
                     f"\n" \
                     f"{ending_mdrk}"

        # 2          тут \n не нужен
        mdrk_var_2 = f"{heading_mdrk}\n" \
                     f"\n" \
                     f"{collect_status_text_gen_2}\n" \
                     f"\n" \
                     f"{physio_conclusion}\n" \
                     f"{lfk_conclusion}\n" \
                     f"\n" \
                     f"{limit_factor}\n" \
                     f"\n" \
                     f"{rehab_potential}\n" \
                     f"\n" \
                     f"{rehab_goals}\n" \
                     f"\n" \
                     f"Клинический диагноз:\n" \
                     f"{diagnosis_complex_2}\n" \
                     f"\n" \
                     f"Реабилитационный диагноз (по МКФ):\n" \
                     f"{rehab_diagnosis_2}\n" \
                     f"\n" \
                     f"{dynamic}\n" \
                     f"\n" \
                     f"{ending_mdrk}"

    elif d['закл_логопеда'] == '' and d['закл_психолога'] != '':
        # 1          тут \n не нужен
        mdrk_var_1 = f"{heading_mdrk}\n" \
                     f"\n" \
                     f"{collect_status_text_gen_1}\n" \
                     f"\n" \
                     f"{physio_conclusion}\n" \
                     f"{lfk_conclusion}\n" \
                     f"\n" \
                     f"{psy_conclusion}\n" \
                     f"\n" \
                     f"{limit_factor}\n" \
                     f"\n" \
                     f"{rehab_potential}\n" \
                     f"\n" \
                     f"{rehab_goals}\n" \
                     f"\n" \
                     f"Клинический диагноз:\n" \
                     f"{diagnosis_complex_1}\n" \
                     f"\n" \
                     f"Реабилитационный диагноз (по МКФ):\n" \
                     f"{rehab_diagnosis_1}\n" \
                     f"\n" \
                     f"{ending_mdrk}"

        # 2          тут \n не нужен
        mdrk_var_2 = f"{heading_mdrk}\n" \
                     f"\n" \
                     f"{collect_status_text_gen_2}\n" \
                     f"\n" \
                     f"{physio_conclusion}\n" \
                     f"{lfk_conclusion}\n" \
                     f"\n" \
                     f"{psy_conclusion_2}\n" \
                     f"\n" \
                     f"{limit_factor}\n" \
                     f"\n" \
                     f"{rehab_potential}\n" \
                     f"\n" \
                     f"{rehab_goals}\n" \
                     f"\n" \
                     f"Клинический диагноз:\n" \
                     f"{diagnosis_complex_2}\n" \
                     f"\n" \
                     f"Реабилитационный диагноз (по МКФ):\n" \
                     f"{rehab_diagnosis_2}\n" \
                     f"\n" \
                     f"{dynamic}\n" \
                     f"\n" \
                     f"{ending_mdrk}"

    elif d['закл_логопеда'] != '' and d['закл_психолога'] != '':
        # 1          тут \n не нужен
        mdrk_var_1 = f"{heading_mdrk}\n" \
                     f"\n" \
                     f"{collect_status_text_gen_1}\n" \
                     f"\n" \
                     f"{physio_conclusion}\n" \
                     f"{lfk_conclusion}\n" \
                     f"\n" \
                     f"{logo_conclusion}\n" \
                     f"\n" \
                     f"{psy_conclusion}\n" \
                     f"\n" \
                     f"{limit_factor}\n" \
                     f"\n" \
                     f"{rehab_potential}\n" \
                     f"\n" \
                     f"{rehab_goals}\n" \
                     f"\n" \
                     f"Клинический диагноз:\n" \
                     f"{diagnosis_complex_1}\n" \
                     f"\n" \
                     f"Реабилитационный диагноз (по МКФ):\n" \
                     f"{rehab_diagnosis_1}\n" \
                     f"\n" \
                     f"{ending_mdrk}"

        # 2          тут \n не нужен
        mdrk_var_2 = f"{heading_mdrk}\n" \
                     f"\n" \
                     f"{collect_status_text_gen_2}\n" \
                     f"\n" \
                     f"{physio_conclusion}\n" \
                     f"{lfk_conclusion}\n" \
                     f"\n" \
                     f"{logo_conclusion_2}\n" \
                     f"\n" \
                     f"{psy_conclusion_2}\n" \
                     f"\n" \
                     f"{limit_factor}\n" \
                     f"\n" \
                     f"{rehab_potential}\n" \
                     f"\n" \
                     f"{rehab_goals}\n" \
                     f"\n" \
                     f"Клинический диагноз:\n" \
                     f"{diagnosis_complex_2}\n" \
                     f"\n" \
                     f"Реабилитационный диагноз (по МКФ):\n" \
                     f"{rehab_diagnosis_2}\n" \
                     f"\n" \
                     f"{dynamic}\n" \
                     f"\n" \
                     f"{ending_mdrk}"

    # сборщик итогового осмотра
    #                  тут \n не нужен
    final_diary = f"{heading_final_diary}\n" \
                  f"\n" \
                  f"Жалобы, на момент осмотра: активно не предъявляет.\n" \
                  f"{st_pr_objectivus}\n" \
                  f"{st_neurologic_gen_2}\n" \
                  f"\n" \
                  f"{dynamic}\n" \
                  f"\n" \
                  f"Диагноз при выписке:\n" \
                  f"{diagnosis_complex_final}\n" \
                  f"\n" \
                  f"{ending_phrase}\n" \
                  f"\n" \
                  f"{ending_final_diary}"

    return {
        'diary_var_1': diary_var_1,
        'diary_var_2': diary_var_2,
        'mdrk_var_1': mdrk_var_1,
        'mdrk_var_2': mdrk_var_2,
        'final_diary': final_diary
    }
