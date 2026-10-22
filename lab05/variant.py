stroka = input("Введите строку: ")
stroka = stroka.split()
count = 0
for i in range(len(stroka)):
    stroka[i] = stroka[i].strip(".,!?;:").lower()
    if stroka[i].startswith(("а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я")):
        print(stroka[i])
        count += 1
if count == 0:
    print("Нет совпадений")
print(f"Количество слов: {count}")
