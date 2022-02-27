my_list = [7, 5, 3, 3, 2]
user_input = input("Введите натуральное число >>> ")
if not user_input.isdigit():
    print("Неверный формат ввода! Введите натуральное число!")
    exit()
user_input = int(user_input)
my_list.append(user_input)
my_list.sort(reverse=True)
print(my_list)
