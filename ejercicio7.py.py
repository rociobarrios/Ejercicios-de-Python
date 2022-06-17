peso=float(input("Cual es tu peso?"));
altura=float(input("Cual es tu altura?"));

imc=round(peso/(altura**2),2);

print("Tu indice de masa corporal es:"+str(imc));
