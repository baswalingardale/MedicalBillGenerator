# This is bill generator for medical
# There many kind of things and features to add this

def create_reciept():
    drug_list = {}
    total = 0
    print("NOTICE : When list is over then type 'end' or 0 to end list")
    while 1:
        drug_name = input("Enter the drug name :\n")
        if drug_name == '0' or drug_name == 'end':
            break
        drug_price = input("Drug price :")
        drug_list[drug_name] = int(drug_price)
    drug_list_second = drug_list.items()


    for drug_name, drug_price in drug_list_second:
        print(drug_name.capitalize(), '\t', drug_price)
        total += drug_price

    print("-------------------------------------------------\nTotal amount :", total)
    return drug_list_second, total