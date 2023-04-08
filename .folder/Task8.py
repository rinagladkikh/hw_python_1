n = int(input("Введите размер шоколадки, длина: "))
m = int(input("Введите размер шоколадки, вторая ширина: "))
k = int(input("Cколько долек хотите отломить: "))
if (k % m == 0 or k % n == 0) and k < m * n:
    print("yes")
else:
    print("no")
