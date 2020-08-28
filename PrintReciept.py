def reciept_print(drug_detail, total):
    print("Do you want print bill :")
    print("1. Yes\n2.No")
    print_command = input()
    if print_command == '1':
        print("YOUR RECIEPT :")
        for drug_name, drug_price in drug_detail:
            print(drug_name, drug_price)
        print("Grand Total :", total)
    elif print_command == '2':
        pass
    else:
        print("Incorrect option.")
        reciept_print(drug_detail, total)
