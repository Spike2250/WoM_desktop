def forming(type_, d):
    if type_ == 'oak':
        return forming_OAK(d)
    elif type_ == 'oam':
        return forming_OAM(d)
    elif type_ == 'bh':
        return forming_BhAK(d)
    elif type_ == 'glucprof':
        return forming_Gluc_profile(d)
    elif type_ == 'my_lab':
        return forming_my_lab(d)


def forming_OAK(d):
    result = f"ОАК от {d['dateEdit_OAK']}: "
    for i in d:
        if i[:5] == 'label':
            a, b = d[i].split(', ')
            result += f"{a} {d[f'lineEdit{i[5:]}']} {b}; "
        elif i == 'lineEdit_OAK_other':
            if len(c := d[i].split(', ')) == 2:
                result += f"{c[0]} {d[f'{i}_r']} {c[1]}; "
            else:
                result += f"{d[i]} - {d[f'{i}_r']}; "

    return result + '\n'


def forming_OAM(d):
    result = f"ОАМ от {d['dateEdit_OAM']}: "
    for i in d:
        if i[:5] == 'label':
            if d[i] == 'Прозрачность':
                result += f"{d[f'lineEdit{i[5:]}']}; "
            elif d[i] == 'Слизь, примеси':
                if d[f'lineEdit{i[5:]}'] in ['+', '++', '+++', '++++']:
                    result += f"Слизь {d[f'lineEdit{i[5:]}']}; "
                elif d[f'lineEdit{i[5:]}'][:3] in ('отр', 'Отр'):
                    result += f"{d[i]} {d[f'lineEdit{i[5:]}']}; "
                else:
                    result += f"Примеси {d[f'lineEdit{i[5:]}']}; "
            else:
                result += f"{d[i]} {d[f'lineEdit{i[5:]}']}; "
        elif i == 'lineEdit_urine_other':
            result += f"{d[i]} {d[f'{i}_r']}; "

    return result + '\n'


def forming_BhAK(d):
    result = f"Б/х анализ крови от {d['dateEdit_BhAK']}: "
    for i in d:
        if i[:5] == 'label':
            a, b = d[i].split(', ')
            result += f"{a} {d[f'lineEdit{i[5:]}']} {b}; "
        elif i in ("lineEdit_bh_other_1",
                   "lineEdit_bh_other_2",
                   "lineEdit_bh_other_3"):
            if len(c := d[i].split(', ')) == 2:
                result += f"{c[0]} {d[f'{i[:-1]}r_{i[-1]}']} {c[1]}; "
            else:
                result += f"{d[i]} - {d[f'{i[:-1]}r_{i[-1]}']}; "

    return result + '\n'


def forming_Gluc_profile(d):
    if d['plainTextEdit_glucprof'] != '':
        result = f"Гликемический профиль от {d['dateEdit_GlucPr']}:\n"\
                 f"  на фоне: {d['plainTextEdit_glucprof']}\n"
    else:
        result = f"Гликемический профиль от {d['dateEdit_GlucPr']}:\n"

    n = 0
    for i in d:
        if i[:5] == 'label':
            n += 1

            if n % 2 != 0:
                result += f"    {d[i]} - {d[f'lineEdit{i[5:]}']}\t    "
            else:
                result += f"{d[i]} - {d[f'lineEdit{i[5:]}']}\n"

    return result + '\n'


def forming_my_lab(d):
    result = f'{d["mylab_name"]} от {d["mylab_date"]}: '
    for i in d:
        if len(i) == 7:
            if len(j := d[i].split(', ')) == 2:
                result += f'{j[0]} {d[f"mylab_r_{i[-1]}"]} {j[1]}; '
            else:
                result += f'{d[i]} {d[f"mylab_r_{i[-1]}"]}; '

    return result + '\n'
