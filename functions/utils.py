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


def sort_by_date():
    """
    Функция сортировки по дате
    """
    executed_operations = state_executed()
    sorting = sorted(executed_operations, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'),
                     reverse=True)
    return sorting


def last_five():
    """
    Функция получения последних 5 операций
    """
    sorting_list = sort_by_date()
    return sorting_list[:5]


def disguise_card(transactions):
    """
    Функция маскировки карты и счета
    """
    for i in transactions:
        if 'перевод' in i['description'].lower():
            if 'счет' in i['from'].lower():
                i['from'] = i['from'][:(len(i['from']) - 4) - 10] + '*' * 6 + i['from'][(len(i['from']) - 4):]
            i['from'] = i['from'][:(len(i['from']) - 4) - 6] + '*' * 6 + i['from'][(len(
                i['from']) - 4):]  # маскировка номера счета отправителя
        i['to'] = i['to'][:(len(i['to']) - 4) - 16] + '*' * 2 + i['to'][(len(
            i['to']) - 4):]  # маскировки номера счета получателя
    return transactions