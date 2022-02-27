"""Не доделано"""

goods = []

count = 1

while True:
    print("Добавить товар - нажмите (1)")
    print("Посмотреть статистику - нажмите (2)")
    print("Выйти - нажмите (0)")
    user_input = int(input())
    if user_input == 1:
        items = {"Название": input("Введите название товара >>> ")}
        if items["Название"] is None:
            break
        items["Цена"] = input("Введите цену товара >>> ")
        if items["Цена"] is None:
            break
        float(items["Цена"])
        items["Количество"] = input("Введите количество товара >>> ")
        if items["Количество"] is False:
            break
        int(items["Количество"])
        items["Ед. измерения"] = input("Введите единицу измерения >>> ")
        if items["Ед. измерения"] is False:
            break
        sku = (count, items)
        goods.append(sku)
        count += 1
        print("Товар успешно добавлен!")
        print("---")
    elif user_input == 2:
        goods_stat = {}

        for i in goods:
            for key, value in i[1].items():
                goods_stat.update(value)
        print(goods_stat)

    elif user_input == 0:
        print("Пока!")
        exit()
    else:
        continue
