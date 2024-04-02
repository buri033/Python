print("Zonas de concentración")
numMaxintegrantes=0; numMenorArmas= 10**100
mayorCantH=0; mayorCantM=0; zonaMayorIntegrantes="";zonaMenorArmas=""
totalH=0; totalM=0; totalIntegrantes=0; totalCantm=0
for i in range(5):
    nomZona=input("Ingresa el nombre de la zona \n")
    numintegrantes= int(input("Ingresa cantidad de integrantes concentrados \n"))
    cantH=int(input("Ingresa la cantidad de de hombres\n"))
    cantM=int(input("Ingresa la cantidad de mujeres\n"))
    cantm=int(input("Ingresa la cantidad de menores de edad\n"))
    numArmas=int(input("Ingresa cantidad de armas a entregar\n"))
    if numintegrantes>numMaxintegrantes:
        numMaxintegrantes=numintegrantes
        zonaMayorIntegrantes=nomZona
    totalH=totalH+cantH
    totalM=totalM+cantM
    totalIntegrantes= totalIntegrantes+numintegrantes
    totalCantm=totalCantm+cantm
    if numArmas<numMenorArmas:
        numMenorArmas=numArmas
        zonaMenorArmas=nomZona
print(f"La zona mayor integrante es: {zonaMayorIntegrantes}")
if totalH>totalM:
    print("Hay más hombres que mujeres concentrados")
elif totalM>totalH:
    print("Hay más mujeres concentradas")
else:
    print("Hay la misma cantidad tanto de hombres, como de mujeres")
porcentajeH=totalH/totalIntegrantes*100
porcentajeM=totalM/totalIntegrantes*100

if porcentajeH>porcentajeM:
    print(f"El porcentaje de hombres es mayor {porcentajeH}%")
elif porcentajeM>porcentajeH:
    print(f"El porcentaje de mujeres es mayor {porcentajeM}%")
else:
    print("Cantidades de hombres y mujeres están en la misma cantidad ")
print(f"El total de menores en las filas es: {totalCantm}")
print(f"La zona que entregará el menor número de armas es: {zonaMenorArmas}")
