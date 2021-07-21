lista = [['Inti',10],['Lucas',12],['Mike',11]]

for recorrido in range(1, len(lista)):
    for posicion in range(len(lista) - recorrido):
        if lista[posicion][1] > lista[posicion + 1][1]:
            temp = lista[posicion]
            lista[posicion] = lista[posicion + 1]
            lista[posicion + 1] = temp
print(lista)