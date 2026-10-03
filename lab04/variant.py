n = int(input("Введите число n: "))
count_values = 0
sum_values = 0
count = 1
for i in range(n):
    chis = int(input(f"Введите число номер {count}: "))
    count += 1
    if abs(chis) % 10 == 2:
        count_values += 1
        sum_values += chis
print(f"Количество удовлетворяющих значений: {count_values}; "
      f"Сумма удовлетворяющих значений: {sum_values}")
