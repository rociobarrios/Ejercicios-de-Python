producto=input("Producto:")
precio=float(input("Precio:"))
unidades=int(input("Unidades:"))

print("{nombre}: ${precio:10.2f} x {unidades:3d}= {total}".format(nombre=producto, precio=precio, unidades=unidades, total= unidades * precio))
