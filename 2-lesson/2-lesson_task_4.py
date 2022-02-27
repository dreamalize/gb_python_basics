user_input = input("Введите список слов через пробел >>> ")
user_input = user_input.split()
for i in range(len(user_input)):
    print(f"{i + 1}.", user_input[i][:10])
