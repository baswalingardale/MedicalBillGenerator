from bill import create_reciept
from PrintReciept import reciept_print


while 1:
    print('''Choose Any one option from following:
1. Create Bill
2. Exit''')
    input_value = input()
    if input_value == '1':
        x, y = create_reciept()
        reciept_print(x, y)
    elif input_value == '2':
        break
    else:
        print("Incorrect option")
