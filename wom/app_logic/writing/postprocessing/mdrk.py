def update_after_mdrk(d):
    update_after_rehab_limits(d)
    update_after_rehab_goals(d)


def update_after_rehab_limits(d):
    lims = ''
    for lim in d['list_limits']:
        lims += f"{lim}; "

    if d['limits_other'] != '':
        lims += d['limits_other']
    if lims[-2:] == '; ':
        lims = lims[:-2]
    d['факторы_ограничивающие_реабилитацию'] = lims


def update_after_rehab_goals(d):
    goals = ''
    for goal in d['list_goals']:
        goals += f"{goal}; "

    if d['goals_other'] != '':
        goals += d['goals_other']
    if goals[-2:] == '; ':
        goals = goals[:-2]
    d['цели_реабилитации'] = goals
