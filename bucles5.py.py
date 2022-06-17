inversion = float(input("Cuanto vas a invertir?"))
interes = float(input("Cuanto es el interes?"))
tiempo = int(input("Cuantos años?"))

for i in range(1, tiempo+1, 1):
    print("En {año} años tu ganancia sera de {ganancia}".format(año=i, ganancia=((inversion/100)*interes)*i))
