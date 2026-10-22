from functions import *


number = int(input("Введите целое число для подсчета суммы цифр его модуля: "))
print(f"Сумма цифр модуля числа: {sum_digits(number)}")



numbers = list(map(int, input("Введите через пробел числа для подсчета среднего арифметического: ").split()))
print(f"Среднее арифметическое чисел: {average(numbers)}" if (average(numbers)) else "Нет данных")


text = input("Введите текст: ")
print(f"Нормализованный текст: {normalize_text(text)}")


numbers = list(map(int, input("Введите целые числа через пробел для проверки на условие: ").split()))
threshold = int(input("Введите порог: "))
print(f"Новый список по условию: {select_numbers(numbers, threshold)}")


text = input("Введите текст")
print(f"Палиндром: {is_palindrome(text)}")
