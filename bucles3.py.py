num = int(input("Escribe un numero entero:"))

if num < 0:
    print("No se permiten numeros negativos")
else:
    for i in range(1, num+1, 2):
        print(i, end=",")
        
