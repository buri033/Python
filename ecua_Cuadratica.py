a = int(input("Digite el valor de a "))
b = int(input("Digite el valor de b "))
c = int(input("Digite el valor de c "))

D= b**2*a*c

X1 = (-b+D**(1/2))/(2*a)
X2 = (-b-D**(1/2))/(2*a)

print("Las raíces son: ")
print("X1: ", X1)
print("X2: ", X2)