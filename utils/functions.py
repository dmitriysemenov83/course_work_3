import json
from datetime import datetime

def get_data():
    with open('C:/project/course_work_3/utils/operations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data

def filtered_data(data):
    operation = [op for op in data if 'state' in op and op['state'] == 'EXECUTED'][-5:]
    operation.reverse()
    return operation


def date_and_data_formatting(operation):
    for op in operation:
        date = datetime.strptime(op['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = op.get('description', 'No description')
        # description = op['description']
        if 'from' in op:
            from_card = op['from']
            card_name, card_number = from_card.split(' ', 1)
            card_number = f"{card_number[:6]}{'*' * 6}{card_number[-4:]}"
            from_card = f"{card_name} {card_number}"
            # from_card = f"{from_card[:6]} {'*' * 6} {from_card[-4:]}"
        else:
            from_card = ""
        to_account = op.get('to', 'No account')
        # to_account = op['to']
        amount = float(op['operationAmount']['amount'])
        currency = op['operationAmount']['currency']['name']
        print(f"{date} {description}")
        print(f"{from_card} -> Счет **{to_account[-4:]}")
        print(f"{amount:.2f} {currency}\n")