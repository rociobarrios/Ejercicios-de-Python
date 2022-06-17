renta = float(input("Cuanto es tu renta anual:"))


if renta >= 60000:
    print("45%")
elif renta <60000 and renta >= 35000:
    print("30%")
elif renta >= 20000 and renta <35000:
    print("20%")
elif renta >= 10000 and renta < 20000:
    print("15%)
else:
    print("5%")
