email=False
mi_email = input("Introduce tu correo: ")

for i in mi_email:
    if(i=="@"):
        email=True
if email:
    print("Email correcto")
else:
    print("Email incorrecto")
