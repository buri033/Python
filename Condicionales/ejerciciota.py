#Se desea conocer la comisión de ventas de cada vendedor de la compañía ABC,
#durante el mes de junio. Hacer un algoritmo que lea el código del vendedor, el
#nombre y sus ventas al mes. La comisión se calculará así:
# Ventas menores a $10000, tienen una comisión del 5%
# Ventas entre $10000 y $20000, comisión del 10%
# Ventas mayores a $20000 comisión del 20%
name = input("Ingrese su nombre: ")
cvendedor = input("Ingrese su codigo de vendedor: ")
venta = int(input("Ingrese la comision de sus ventas al mes"))
if venta < 10000:
    comision = venta * 0.05
    print("su comicion es: ",comision)
else:
    if venta >= 10000 and venta <= 20000:
        comision = venta * 0.1
        print("su comicion es: ",comision)
    else:
        if venta >20000:
            comision = venta * 0.20
            print("su comicion es: ",comision)

