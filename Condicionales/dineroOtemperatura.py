temperatura= float(input("Ingrese la temperatura"))
dinero= float(input("Ingrese el dinero"))

if (temperatura >30):
    print("Hace calor")
    if(dinero>5000):
        print("Compra un helado")
    elif(dinero<=5000 and dinero>0):
        print("Toma agua")
else:
    (temperatura<=30)
    print("Hace frio")
