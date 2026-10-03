first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))
operation = input("Введите одну из операций: +, -, *, /: ")
if operation == "/" and second == 0:
    print("Деление на ноль запрещено")
elif operation not in "+-/*":
    print("Неизвестна операция")
else:
    if operation == "+":
        print(f"Результат: {first + second:.2f}")
    elif operation == "-":
        print(f"Результат: {first - second:.2f}")
    elif operation == "*":
        print(f"Результат: {first * second:.2f}")
    elif operation == "/":
        print(f"Результат: {first / second:.2f}")
