num = int(input("Escribe un numero entero positivo mayor a 1"))
cont=0
for divisor in range(1, num+1):
    if num%divisor == 0:
        print("{num}/{divisor}={resultado}".format(num=num, divisor=divisor, resultado= num/divisor))
        cont+=1
if cont == 2:
    print("Es primo")
else:
    print("No es primo")

#cont=2
        
