print("Pizzeria Bella Napoli".upper())
respuesta=input("Quieres una pizza Vegetariana? (S o N)")

if respuesta.lower() == "s":
    ingrediente= int(input("Elige el ingrediente de tu pizza: 1-Pimiento/n 2-Tofu"))
    if ingrediente == 1:
        print("Tu pizza llevara: Pimiento/nMozzarella/nTomate")
    elif ingrediente == 2:
        print("Tu pizza llevara: Tofu/nMozzarella/nTomate")
    else:
        print("ERROR")
    else:
        ingrediente= int(input("Elige el ingrediente de tu pizza: 1-Peperoni/n 2-Jamon/n 3-Salmon"))
    if ingrediente == 1:
        print("Tu pizza llevara: Peperoni/nMozzarella/nTomate")
    elif ingrediente == 2:
        print("Tu pizza llevara: Jamon/nMozzarella/nTomate")
    elif ingrediente == 3:
        print("Tu pizza llevara: Salmon/nMozzarella/nTomate")
    else:
        print("ERROR")
