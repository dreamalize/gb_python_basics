user_num = int(input("Введите целое положительное число >>> "))
max_digit = 0
while True:
    if (user_num // 10) == 0:
        if user_num > max_digit:
            max_digit = user_num
            print(max_digit)
            break
        else:
            print(max_digit)
            break
    else:
        remainder = user_num % 10
        user_num = user_num // 10
        if remainder > max_digit:
            max_digit = remainder
            continue



