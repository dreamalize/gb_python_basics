"""В задании не указано, но судя по всему n - целое положительное число
На всякий случай добавил abs()"""

user_num = int(input("Введите целое положительное число >>> "))
user_num = abs(user_num)
str_num = str(user_num)
double_num = str_num + str_num
triple_num = double_num + str_num
result = int(str_num) + int(double_num) + int(triple_num)
print(result)
