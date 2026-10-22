stroka = input("Введите строку: ")
zam = stroka.count(":")
stroka = stroka.replace(":", "-")
print(f"Количество замен: {zam} | Новая строка: {stroka}")
