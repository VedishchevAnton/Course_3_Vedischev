from functions import utils
import requests
import pytest


# def test_load_json():
#     """
#     Тестирование функции получения данных из json файла
#     """
#     assert type(utils.load_json()) == list
#     assert len((utils.load_json())) > 0
#

def test_state_executed():
    """
    Тестирование функции получения списка выполненных операций
    """
    assert isinstance(utils.state_executed(), list)
    assert utils.state_executed() is not None


