user_input = input("Введите значения для списк через пробел >>> ")
my_list = user_input.split()
for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(f"Результат: {my_list}")


"""Альтернативный вариант через цикл while
смена происходит после каждого ввода занчеия пользователем"""
# my_list = []
# while True:
#     user_input = input("Введите значение для списка >>> ")
#     my_list.append(user_input)
#     for i in range(0, len(my_list)-1, 2):
#         my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
#     print(f"Результат: {my_list}")
