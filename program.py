estados_animos = False
name_user = input("Introduzca su usuario: ")
eleccion = input("Bienvenido " + name_user + " esconja entre los siguientes estados de animo: feliz, alegre, cansado, agotado: ")

if ((eleccion == "feliz") or (eleccion == "alegre")):
        estados_animos = True
if estados_animos:
    print("Tenemos una pregunta para ti")
else:
    print("Puede ingresar a la sala")

