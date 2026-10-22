stroka = input("Введите строку: ")
probstr = stroka.strip()
while "  " in probstr:
    probstr = probstr.replace("  ", " ")
print(f"Исходная длина: {len(stroka)} | Новая длина: {len(probstr)}")
print(f"Нормализованный текст: {probstr} | Количество слов: {len(probstr.split())}")
