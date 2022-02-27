user_input = input("Введите порядковый номер месяца >>> ")
if not user_input.isdigit():
    print("Введите целое число")
    exit()
user_input = int(user_input)
if user_input not in range(1, 13):
    print("Введите целое число от 1 до 12")
    exit()

winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

months = {"Зима": winter, "Весна": spring, "Лето": summer, "Осень": autumn}
for key, value in months.items():
    if user_input in value:
        print(key)
