fecha = input("Escribe tu fecha de nacimiento en formato: ")


dia=fecha[:fecha.find("/")]
mesaño=fecha[fecha.find("/")+1:]

mes=mesaño[:mesaño.find("/")]
año=mesaño[mesaño.find("/")+1:]


print(dia)
print(mes)
print(año)
