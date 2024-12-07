refrigerator = {
    "мясо": {},
    "овощи": {},
    "молоко": {},
    "другое": {}
}

def receive_batch(batch, refrigerator):
    """Добавляет партию продуктов в холодильник."""
    for value in batch.values():
        if value['тип'] == refrigerator['мясо']:
            refrigerator['мясо'].append({value['название']:{'количество': value['количество']}})
        elif value['тип'] == refrigerator['овощи']:
            refrigerator['овощи'].append({value['название']:{'количество': value['количество']}})
        elif value['тип'] == refrigerator['молоко']:
            refrigerator['молоко'].append({value['название']:{'количество': value['количество']}})
        elif value['тип'] == refrigerator['другое']:
            refrigerator['другое'].append({value['название']:{'количество': value['количество']}})
        for i in refrigerator.values():
            if value['название'] in i:
                value['количество'] += i['количество']
    print(refrigerator)


def view_product(product_name, refrigerator):
    """Просматривает информацию о конкретном продукте."""
    if product_name in refrigerator:
        for value, key in refrigerator.items():
            if value['название'] == product_name:
                s = value['название'] + key + str(value['количество'])
                print(s)
    else:
        print('Данного продукта нету в холодильнике :(')

def remove_product(product_name, refrigerator):
    """Удаляет продукт из холодильника."""
    if product_name in refrigerator:
        for value in refrigerator.values():
            if product_name == value['название']:
                refrigerator.pop(value)
    else:
        print('Данного продукта нету в холодильнике :(')


def sell_product(product_name, quantity, refrigerator):
    """Продаёт указанное количество продукта."""
    if product_name in refrigerator:
        if (refrigerator[product_name]['количество'] - quantity) < 0:
            print('Недостаточно продуктов')
            return None
        refrigerator[product_name]['количество'] -= quantity
        print(refrigerator)
    else:
        print('Данного продукта нету в холодильнике :(')



# Пример использования (для тестирования):
batch = {
    1: {"название": "говядина", "тип": "мясо", "количество": 100},
    2: {"название": "картофель", "тип": "овощи", "количество": 500}
}

receive_batch(batch, refrigerator)
view_product("говядина", refrigerator)
sell_product("говядина", 50, refrigerator)
view_product("говядина", refrigerator)
remove_product("говядина", refrigerator)
view_product("говядина", refrigerator)