from utils.functions import print_last_operations
import json
import tempfile
from pathlib import Path
import pytest


@pytest.fixture
def test_data():
    data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        }
    ]

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        json.dump(data, f)

    yield f.name

    Path(f.name).unlink()


def test_print_last_operations(test_data, capsys):
    print_last_operations(test_data)

    expected_output = ['23.03.2019 Перевод со счета на счет',
 'Счет 448122******4719 -> Счет **1160',
 '43318.34 руб.',
 '',
 '04.04.2019 Перевод со счета на счет',
 'Счет 197086******8542 -> Счет **4188',
 '79114.93 USD',
 '',
 '23.03.2018 Открытие вклада',
 ' -> Счет **2431',
 '48223.05 руб.',
 '',
 '30.06.2018 Перевод организации',
 'Счет 751068******6952 -> Счет **6702',
 '9824.07 USD',
 '',
 '03.07.2019 Перевод организации',
 'MasterCard 715830******6758 -> Счет **5560',
 '8221.37 USD',
 '']

    captured_output = capsys.readouterr().out.split("\n")[:-1]

    assert captured_output == expected_output
