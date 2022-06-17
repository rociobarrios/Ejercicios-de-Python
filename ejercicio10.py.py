muñecas=int(input("Numero de muñecas en el pedido: "));
payasos=int(input("Numero de payasos en el pedido: "));

pesoMu=int(muñecas*75);
pesoPa=int(payasos*112);

pesoTotal=pesoMu+pesoPa;

pesoTkg=pesoTotal/1000;

print("El peso es de: "+str(pesoTkg)+"Kg");
