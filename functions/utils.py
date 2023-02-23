import requests
import datetime
from data_link import DATA_SOURCE


def load_json():
    """
    Получение данных из json файла
    """
    data = requests.get(DATA_SOURCE)
    data_words = data.json()
    return data_words
