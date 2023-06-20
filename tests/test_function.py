import pytest
from utils.functions import get_data, filtered_data, date_and_data_formatting

def test_get_data():
    data = get_data()
    assert isinstance(data, list)

def test_filtered_data(test_data):
    date = filtered_data(test_data)
    assert len(date) == 5

def test_date_and_data_formatting(test_data, capsys):
    date_and_data_formatting(test_data)

    expected_output = ['26.08.2019 Перевод организации',
 'Maestro 159683******5199 -> Счет **9589',
 '31957.58 руб.',
 '',
 '03.07.2019 Перевод организации',
 'MasterCard 715830******6758 -> Счет **5560',
 '8221.37 USD',
 '',
 '30.06.2018 Перевод организации',
 'Счет 751068******6952 -> Счет **6702',
 '9824.07 USD',
 '',
 '23.03.2018 Открытие вклада',
 ' -> Счет **2431',
 '48223.05 руб.',
 '',
 '04.04.2019 Перевод со счета на счет',
 'Счет 197086******8542 -> Счет **4188',
 '79114.93 USD',
 '',
 '23.03.2019 Перевод со счета на счет',
 'Счет 448122******4719 -> Счет **1160',
 '43318.34 руб.',
 '']

    captured_output = capsys.readouterr().out.split("\n")[:-1]

    assert captured_output == expected_output