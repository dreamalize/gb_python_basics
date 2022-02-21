user_num = int(input("Введите целое положительное число >>> "))
max_digit = 0
while True:
    if (user_num // 10) == 0:
        max_digit = user_num
        break
    # remainder = user_num % 10
    if user_num % 10 == 0:
        user_num = user_num // 10
        continue
print(max_digit)

