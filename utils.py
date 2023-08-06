import json
import datetime


def load_operations():
    """
    открываем файл с операциями
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        return json.load(file)


card_operations = load_operations()


def get_date_sort():
    """
    :return: даты последних 5-ти операций
    """
    date_operations = []
    for operation in card_operations:
        if "date" in operation:
            date_operations.append(operation['date'])
        date_operations.sort()
    return date_operations[-5:]


def format_from(operation_from):
    """
    привидение вывода к определенному стандарту
    :param operation_from: ввод название счета/карты
    :return:
    """
    if operation_from[0] == "С":
        return operation_from[:5] + '**' + operation_from[-4:]
    else:
        return operation_from[:-12] + '** **** ' + operation_from[-4:]


def print_operations():
    """
    :return: вывод статистики в нужном формате
    """
    date_operations = get_date_sort()
    date_operations.reverse()
    for payment_date in date_operations:
        for operation in card_operations:
            if "date" in operation:
                if operation['date'] == payment_date:
                    date_operation = datetime.datetime.strptime(payment_date, '%Y-%m-%dT%H:%M:%S.%f')
                    print(f"""{date_operation.strftime("%d.%m.%Y")} {operation["description"]}
{format_from(operation["from"]) if 'from' in operation else ""} -> {format_from(operation["to"])}
{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n""")
