number = int(input("Введите насколько заполнен архив: "))
if 0 <= number <= 44:
    print("Есть место")
elif 45 <= number <= 94:
    print("Архив растёт")
elif 95 <= number <= 100:
    print("Почти заполнен")
else:
    print("Ошибка диапазона")
