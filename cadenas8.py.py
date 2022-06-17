precio = input("Introduce el precio: ")

print("Euros: ", precio[:precio.find(".")], "Centimos: ", precio[precio.find("."):])
