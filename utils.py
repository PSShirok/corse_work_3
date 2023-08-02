import json


def load_operations():
    """
    открываем файл с операциями
    :rtype: object
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        return json.load(file)


card_operations = load_operations()


def get_date_sort():
    date_operations = []
    for operation in card_operations:
        if "date" in operation:
            date_operations.append(operation['date'])
        date_operations.sort()
    return date_operations[-5:]