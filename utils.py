import json

def load_operations():
    """
    открываем файл с операциями
    :rtype: object
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        return json.load(file)
