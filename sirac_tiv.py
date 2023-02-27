import json

def ask_number():
    """harcnum e sirac tivy"""
    num = input('mutqagreq dzer sireli tivy: ')

    filename = 'num.json'
    with open (filename, 'w') as f:
        json.dump(num, f)
    print('dzer sireli tivy: ' + num + '!')
ask_number()


