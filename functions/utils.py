import requests
import datetime


def load_json():
    """
    Функция получения данных из json файла
    """
    data = requests.get('https://api.npoint.io/ce6d4e606f2fd82a0d68')
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


def date_format_change(transactions):
    """
    Функция изменения формата даты
    """
    disguise_card(transactions)
    for i in transactions:
        # Приводим дату к нужному формату без посторонних символов, затем изменяем формат на нужный.
        i['date'] = (datetime.datetime.strptime(i['date'], "%Y-%m-%dT%H:%M:%S.%f")).strftime("%d.%m.%Y")
    return transactions


def output(transactions):
    """
    Функция вывода операций
    """
    date_format_change(transactions)
    for i in transactions:
        if 'Открытие вклада' in i['description']:
            print(f"{i['date']} {i['description']}\n"
                  f"{i['to']}\n"
                  f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
            print()
        elif 'Перевод со счета на счет' or 'Перевод организации' or 'Перевод с карты на карту' in i['description']:
            print(f"{i['date']} {i['description']}\n"
                  f"{i['from']} -> {i['to']}\n"
                  f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
            print()


def main():
    output(last_five())
