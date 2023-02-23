from functions import utils
import requests
import pytest


def test_load_json():
    """
    Тестирование функции получения данных из json файла
    """
    assert type(utils.load_json()) == list

