"""Сначала сделала как описано, но потом подумал,
если это типа электронные часы, то еще добавил корректное отображение
часов, если значение больше 24"""
user_time = int(input("Введите колво секунд >>> "))
sec_time = user_time % 60
sec_time_1 = sec_time // 10
sec_time_2 = sec_time % 10
min_time = user_time // 60 % 60
min_time_1 = min_time // 10
min_time_2 = min_time % 10
hours_time = user_time // 60 // 60
hours_time_1 = hours_time % 24 // 10
hours_time_2 = hours_time % 24 % 10

print(f'{hours_time_1}{hours_time_2}:{min_time_1}{min_time_2}:{sec_time_1}{sec_time_2}')
