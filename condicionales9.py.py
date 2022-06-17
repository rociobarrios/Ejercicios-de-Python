edad = int(input("Cual es la edad del cliente:"))

if edad <= 4:
    print("Entrada Gratis")
elif edad > 4 and edad <= 18:
    print("Entrada 5€")
else:
    print("Entrada 10€")
