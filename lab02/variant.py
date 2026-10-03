total = int(input("Введите количество порций: "))
capacity = int(input("Введите количество порций на подносе: "))
print(f"Полностью заполненных подносов: {total // capacity} \nОсталось: {total % capacity} \nПачек: {(total + capacity - 1) // capacity}")
