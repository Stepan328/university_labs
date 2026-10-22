numbers = list(map(int, input("Введите целые числа через пробел: ".split())))
index = 0
while index < len(numbers):
    if numbers[index] in numbers[:index]:
        numbers.pop(index)
    else:
        index += 1
print(numbers)
