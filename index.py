
# nombre = input("Introduce tu nombre")
# print("hola" + nombre + "!")


# horas = float(input ("Introduce tus horas de trabajo: "))
# coste = float(input("Introduce lo que cobras por horas: "))
# paga = horas * coste
# print("tu paga es", paga)

# paga = 2000

# if paga < 3000:
#     print("Felicitaciones por tu paga")
# else:
#     print("Debes trabajar más duro")


nombre = input("Introduce tu nombre")
print("bienvenido" + nombre + "!")

peso = input("¿Cual es tu peso en kg?")
estatura = input("¿Cual es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("tu índice de masa corporal es" + str(imc))