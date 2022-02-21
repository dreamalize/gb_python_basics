result = int(input("Результат спортсмена в первый день >>> "))
target = int(input("Целевая дистанция спортсмена >>> "))
improvement_per_day = 0.1
day_counter = 1
while result < target:
    result += result * improvement_per_day
    day_counter += 1
print(f"Спортсмен достигнет результата - не менее {target} км. в день, на {day_counter}-й день пробежек")
