import requests
import datetime
from data_link import DATA_SOURCE


def load_json():
    """
    Функция получения данных из json файла
    """
    data = requests.get(DATA_SOURCE)
    data_words = data.json()
    return data_words


def state_executed():
    """
    Функция получения списка выполненных операций
    """
    executed_data = load_json()
    list_executed = []
    for i in executed_data:
        if not i:
            continue
        else:
            if i['state'] == "EXECUTED":
                list_executed.append(i)

    return list_executed
