num = int(input("Escribe un numero entero:"))

if num < 0:
    print("No se permiten numeros negativos")
else:
    for i in range(num,0,-1):
        print(i, end=",")
