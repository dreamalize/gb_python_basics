revenue = int(input("Введите значение выручки (руб.) >>> "))
cost = int(input("Введите значение издержек (руб.) >>> "))
if revenue < cost:
    print("Ваша фирма работает в убыток :( Нужно что-то менять...")
elif revenue == cost:
    print("Ваша фирма работает в ноль... Подумайте, как начать получать прибыль")
else:
    print("Ваша фирма приносит прибыль!")
    profit_ratio = round(((revenue - cost) / revenue * 100), 2)
    print("Рентабельность выручки: {}%".format(profit_ratio))
    employers = int(input("Введите кол-во сотрудников >>> "))
    profit_per_employer = round(((revenue - cost) / employers), 2)
    print("Ваша компания зарабатывает {} руб. на одного сотрудника".format(profit_per_employer))
