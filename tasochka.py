inventory = {
    "apple": {"quantity": 100, "price": 1.0},  # Словарь инвентаря: название товара - словарь с количеством и ценой
    "banana": {"quantity": 50, "price": 0.5},
    "orange": {"quantity": 75, "price": 0.75}}
item = inventory.keys()
quantity = inventory.values()
price = inventory.values()
def restock(item:str,quantity:int,price:float,inventory:dict):
    """Пополняет склад."""
    if item in inventory:
        inventory[item]['quantity'] += quantity
        inventory[item]['price'] += price
    else:
        print('Данного товара нет в наличии :( .')




def sell(inventory, item, quantity, price):
    """Продаёт товары и возвращает выручку."""


    if item in inventory:
        if (inventory[item]["quantity"] - quantity) < 0:
            print('Недостаточно продуктов')
            return None
        inventory[item]["quantity"] -= quantity
        try:
            print('Количество продукта: ', inventory[item][quantity])
        except KeyError:
            print('Бим-бам')
        moneys = inventory[item]['price'] * quantity

        print('Ваша выручка составила: ', moneys)
    else:
        print('Данного товара нет в наличии :( .')





def generate_report(inventory:dict)->str:
    """Генерирует отчёт о текущем состоянии склада."""
    summ = 0
    s = ''
    for value in inventory.values():
        summ += value['quantity'] * value['price']
    for key,value in inventory.items():
        print(key,value["quantity"],value['price'])
        s += key + str(value['quantity']) + str(value['price']) + '\n'

    return s+'\n'+str(summ)

# Main game loop (основной цикл игры)
while True:
    com = input('Введите комманду: \n 1.restock - пополнение товара. \n 2.sell - продажа товара. \n 3.generate_report - составить отчёт о состоянии склада. \n 4.stop - остановить программу.')
    if com == '1':
        item = input('Введите наименование товара: ')
        quantity = int(input('Введи кол-во товара: '))
        price = float(input('Введи цену товара :'))
        restock(item,quantity,price,inventory)
    elif com == '2':
        item = input('Введите наименование товара, который вы хотите продать: ')
        quantity = int(input('Введите кол-во товара, которое вы хотите продать: '))
        sell(inventory, item, quantity, price)
    elif com == '3':
        print(generate_report(inventory))
    elif com == '4':
        break
    else:
        print('Данной команды не существует.')
