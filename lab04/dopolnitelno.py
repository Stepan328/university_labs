chis = int(input("Введите число: "))
for i in range(2, int(chis**0.5) + 1):
    if chis % i == 0:
        print("Число составное")
        break
else:
    print("Число простое")
