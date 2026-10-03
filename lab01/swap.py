first_room = input("Введите название первой аудитории: ")
second_room = input("Введите название второй аудитории: ")
print(f"\nИсходные значения: \nПервая аудитория: {first_room} \nВторая аудитория: {second_room}")
three = first_room
first_room = second_room
second_room = three
print(f"Значения после замены местами: \nПервая аудитория: {first_room} \nВторая аудитория: {second_room}")
