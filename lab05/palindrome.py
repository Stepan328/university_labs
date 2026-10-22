stroka = input("Введите строку: ")
stroka = "".join(stroka.lower().split())
if len(stroka) == 0:
    print("Нет текста")
else:
    if stroka == stroka[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")
