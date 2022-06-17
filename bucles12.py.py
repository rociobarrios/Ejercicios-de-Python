frase = input("Escribe una frase:")   #Rocio
letra = input("Escribe una letra:")   #e
cont=0
for i in frase:
    if i == letra:
        cont+=1


print("La letra " + letra + " aparece " + str(cont) + " veces ")
