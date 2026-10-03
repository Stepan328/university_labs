order_name = input("Введите название заказа: ")
customer_name = input("Введите имя заказчика: ")
first_pos_name = input("Введите название первой позиции: ")
first_pos_count = int(input("Введите количество первой позиции: "))
first_pos_cost = float(input("Введите цену первой позиции: "))
second_pos_name = input("Введите название второй позиции: ")
second_pos_count = int(input("Введите количество второй позиции: "))
second_pos_cost = float(input("Введите цену второй позиции: "))
delivery_cost = float(input("Введите стоимость доставки: "))
inputed_money = float(input("Введите внесённую стоимость: "))
discount = float(input("Введите скидку на заказ (в %): ")) / 100
first_pos_total_cost = first_pos_cost * first_pos_count
second_pos_total_cost = second_pos_cost * second_pos_count
total_cost_without_delivery = first_pos_total_cost + second_pos_total_cost
total_cost_with_delivery = first_pos_total_cost + second_pos_total_cost + delivery_cost
total_cost_with_delivery_discount = first_pos_total_cost * (1 - discount) + second_pos_total_cost * (
            1 - discount) + delivery_cost
total_pos_count = first_pos_count + second_pos_count
change = inputed_money - total_cost_with_delivery_discount
print(f"\n\tЗаказ: {order_name} от {customer_name} | с учётом скидок (в п. Дополнительно)")
print(f"Название: {first_pos_name} | Количество: {first_pos_count} | Цена: {first_pos_cost * (1 - discount):.2f} руб | Стоимость: {first_pos_total_cost * (1 - discount):.2f} руб")
print(f"Название: {second_pos_name} | Количество: {second_pos_count} | Цена: {second_pos_cost * (1 - discount):.2f} руб | Стоимость: {second_pos_total_cost * (1 - discount):.2f} руб")
print(f"Общая сумма заказа с доставкой: {total_cost_with_delivery:.2f} руб / без доставки {total_cost_without_delivery * (1 - discount):.2f} руб\nОбщее количество товара: {total_pos_count}\nСкидка: {total_cost_with_delivery - total_cost_with_delivery_discount} руб. ({discount}%)\nСдача: {change:.2f} руб")
