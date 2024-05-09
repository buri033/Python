import random as rd


def sumaMeses(MS):
    VSC = [0] * 6
    for j in range(6):
        sc = 0
        for i in range(5):
            sc += MS[i][j]
        VSC[j] = sc
    return VSC


def mesMasSolicitado(VSC):
    maxi = VSC[0]; mesM = 0
    for i in range(6):
        if VSC[i] > maxi:
            maxi = VSC[i]
            mesM = i
    return mesM
def serviciosMS(MS):
    VSF = [0] * 5; sm = ""
    for i in range(5):
        sf = 0
        for j in range(6):
            sf += MS[i][j]
        VSF[i] = sf
    maxi = VSF[0]
    for i in range(5):
        if VSF[i] > maxi:
             maxi = VSF[i]
             sm = i
    return sm


# principal
MS = []
for i in range(5):
    MS.append([0] * 6)
for i in range(5):
    for j in range(6):
        MS[i][j] = rd.randint(0, 10)
for i in MS:
    print(i)
VSC = sumaMeses(MS)
print("El total de servicios en cada mes fue: ", VSC)
maxi = mesMasSolicitado(VSC)
print("El mes con mayor demanda  fue: ", maxi)
sm = serviciosMS(MS)
print("El servicio mas solicitado fue: ", sm)