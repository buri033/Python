#Para un cajero electrónico se requiere un algoritmo que determine la cantidad menor de billetes a entregar
# a un cliente, para ello se cuenta con las denominaciones de $10mil, $20mil, $50mil, $100000. Además el algoritmo,
#debe validar si el usuario tiene fondos suficientes para ese retiro y además, que el monto solicitado sea multiplo
#de 10

saldo= 5000000
opcion1= 0
opcion2= 0
opcion3= 0
opcion4= 0


retiro= float(input("Ingrese el valor que quiere retirar: "))
retiro= retiro
if retiro<saldo:
    if retiro%10000==0:
        pendiente= retiro
        opcion1= pendiente //100000
        pendiente=pendiente-opcion1*100000
        opcion2= pendiente // 50000
        pendiente= pendiente-opcion2*50000
        opcion3= pendiente// 20000
        pendiente= pendiente-opcion3*20000
        opcion4= pendiente//10000
    else:
        print("Monto debe ser multiplo de 10000")
else:
    print("Sin saldo mijo")
print("La cantidad de billetes de 100 es: ", int(opcion1), "\nLa cantidad de billetes de 50 es: ", int(opcion2), "\nLa cantidad de billetes de 20 es: ", int(opcion3), "\nLa cantidad de billetes de 10 es: ", int(opcion4))
