first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
if first <= second and first <= third:
    print(f"Минимальное число: {first}")
elif second <= first and second <= third:
    print(f"Минимальное число: {second}")
else:
    print(f"Минимальное число: {third}")
