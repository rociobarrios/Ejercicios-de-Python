num = int(input("Escribe un numero entero positivo:"))

for i in range(1, num, 2):
    print("/")
    for j in range(i, o, -2):
        print(j, end="")
