def create_purchase_dict(*items):
    purchase_dict = {}
    for item in items:
        name, price = item
        purchase_dict[name] = price
    return purchase_dict

# Пример вызова функции с указанными вами входными данными
items = [("Кружка", 300), ("Стакан", 400), ("кофе 500 гр", 800)]
result = create_purchase_dict(*items)
print(result)