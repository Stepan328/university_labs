def palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return palindrome(text[1:-1])


text = input("Введите строку для проверки на палиндром: ")
text = "".join(text.lower().split())
if len(text) == 0:
    print("Нет данных")
else:
    pal = palindrome(text)
    print("Палиндром" if pal else "Не палиндром")
