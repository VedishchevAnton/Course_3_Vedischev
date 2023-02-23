from functions import utils
import requests
import pytest


def test_load_json():
    """
    Тестирование функции получения данных из json файла
    """
    assert type(utils.load_json()) == list
    assert len((utils.load_json())) > 0


def test_state_executed():
    """
    Тестирование функции получения списка выполненных операций
    """
    assert isinstance(utils.state_executed(), list)
    assert utils.state_executed() is not None


def test_sort_by_date():
    """"
    Тестирование функции сортировки по дате
    """
    assert isinstance(utils.sort_by_date(), list)
    assert utils.state_executed() != utils.sort_by_date()


def test_last_five():
    """"
    Тестирование функции получения последних 5 операций
    """
    assert isinstance(utils.last_five()[:5], list)
    assert len(utils.last_five()[:5]) == 5

def test_disguise_card():
    """
    Тестирование функции маскировки карты и счета
    """
    for i in utils.last_five()[:5]:
        assert isinstance(i, dict)

    last_five_transactions = utils.last_five()[:5]
    assert isinstance(utils.disguise_card(last_five_transactions), list)



