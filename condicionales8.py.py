bonificacion=2400

puntos = float(input("Cual es el puntaje del empleado:"))

if puntos > 0 and puntos <0.4:
    print("ERROR")
elif puntos > 0.4 and puntos < 0.6:
    print("ERROR")
elif puntos == 0:
    print("INACEPTABLE")
    PRINT("Dinero que recibiras:", bonificacion*puntos)
elif puntos == 0.4:
    print("ACEPTABLE")
    print("Dinero que recibiras:", bonificacion*puntos)
elif puntos > 0.6:
    print("MERITORIO")
    print("Dinero que recibiras:", bonificacion*puntos)
