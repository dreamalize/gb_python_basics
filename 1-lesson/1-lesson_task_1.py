title = "Анкета пользователя"

print(title)
print("---")

user_name = input("Введите Ваше Имя: ")
user_lastname = input("Введите Вашу Фамилию: ")
user_age = int(input("Ввеите Ваш возраст: "))
user_city = input("Из какого Вы города: ")
user_phone = input("Введите ваше телефон: ")
print()
print("--- Спасибо! Ваши данные записаны ---")
print(user_name, user_lastname)
print(f"Возраст: {user_age}")
print("Город: {}, Телефон: {}".format(user_city, user_phone))
