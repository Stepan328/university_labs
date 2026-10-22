sp_chis_old = list(map(int, input("Введите целые числа через пробел: ").split()))
sp_chis_new = [abs(chislo) for chislo in sp_chis_old]
print(f"Исходный список: {sp_chis_old} | Новый список: {sp_chis_new}")
