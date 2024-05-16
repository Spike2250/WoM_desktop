from wom.app_logic.handbooks.scale import rehab_routing
from wom.settings.config import bed_profiles


def update(d):
    RULES = {
        bed_profiles[0]: rehab_routing['central_neuro'],
        bed_profiles[1]: rehab_routing['trauma'],
        bed_profiles[2]: rehab_routing['somatic']
    }
    for rule in RULES:
        if d['профиль_коек'] == rule:
            d['ШРМ_описание'] = RULES[rule]
