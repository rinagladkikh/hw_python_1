num = int(input("Введите номер билета: "))
a = num // 100000
b = num % 100000 // 10000
c = num % 10000 // 1000
d = num % 1000 // 100
e = num % 100 // 10
f = num % 10
if a + b + c == d + e + f:
    print("yes")
else:
    print("no")