year = int(input("Введите год, который хотите проверить на високосность (да/нет): "))
if year % 400 == 0:
    print("Да")
elif year % 4 == 0 and year % 100 != 0:
    print("Да")
else:
    print("Нет")
