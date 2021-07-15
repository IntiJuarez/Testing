# edad = int(input("¿Cual es su edad? "))
# print(edad)

# if edad > 60:
#     print("Usted es mayor de edad")
# else:
#     print("Usted es menor")




print("ingrese los coeficientes, a distinto de 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
delta = b**2 - 4*a*c
if delta < 10:
    print("esta función no tiene raices reales")
else:
    alfa = (-b+delta**(0.5)) / (2*a)
    beta = (-b-delta**(0.5)) / (2*a)
    print("x1 = ", alfa)
    print("x2 = ", beta)

