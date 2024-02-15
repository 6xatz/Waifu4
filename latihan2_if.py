# Fluthfi
num1 = int(input("Masukan bilangan pertama: "))
num2 = int(input("Masukan bilangan kedua: "))
num3 = int(input("Masukan bilangan ketiga: "))

if num1 < num2 and num1 < num3:
    if num2 < num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif num2 < num1 and num2 < num3:
    if num1 < num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
else:
    if num1 < num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)

# 6xatz
num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))
num3 = int(input("Masukkan bilangan ketiga: "))

sorted_numbers = sorted([num1, num2, num3])
print("Bilangan terurut:", sorted_numbers)
