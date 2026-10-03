first_subject = input("Введите название 1-го предмета: ")
first_classes = int(input("Введите количество занятий по 1-ому предмету: "))
first_time = int(input("Введите время 1-го занятия  в минутах: "))
second_subject = input("Введите название 2-го предмета: ")
second_classes = int(input("Введите количество занятий по 2-ому предмету: "))
second_time = int(input("Введите время 2-го занятия  в минутах: "))
time_normal = int(input("Введите доступное время на неделю в часах: "))
if first_classes >= 0 and second_classes >= 0 and first_time > 0 and second_time > 0 \
    and time_normal * 60 >= (first_classes * first_time + second_classes * second_time):
    print(f"\nВремя для 1-го предмета: {first_classes * first_time} минут")
    print(f"Время для 2-го предмета: {second_classes * second_time} минут")
    print(f"Общая нагрузка: {first_classes * first_time + second_classes * second_time} минут"
          f" или {(first_classes * first_time + second_classes * second_time) / 60 :.2f} часов")
    print(f"Остаток свободного времени: {time_normal - (first_classes * first_time + second_classes * second_time) / 60 :.2f} часов")
    print(f"Нагрузка за четыре одинаковые недели: {(first_classes * first_time + second_classes * second_time) * 4 / 60 :.2f} часов")
