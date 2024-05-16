from prettytable import PrettyTable


def update_after_bta_protocol(d):
    muscles = d['бта_мышцы']
    # создаем таблицу мышц-мишеней
    table = PrettyTable()
    fields = ["Название инъецированной мышцы",
              "Доза БТ-А, Ед."]
    table.field_names = fields

    for m in muscles:
        fullname = f"{m['muscle']} - {m['side']}"
        table.add_row([fullname, m['dose']])

    d['БТА_мышцы_мишени'] = str(table)
