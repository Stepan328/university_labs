a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a < b:
    for chis in range(a, b + 1):
        print(chis)
elif a > b:
    for chis in range(a, b - 1, -1):
        print(chis)
elif a == b:
    print(a)
