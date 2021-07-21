corredores_10k = [['Lucas',34],['Mike',36],['Inti',29],['Nacho',37]]

for i in range(1, len(corredores_10k)):
    for a in range(len(corredores_10k) -i):
        if (corredores_10k[a][1] > corredores_10k[a + 1][1]):
            temp = corredores_10k[a]
            corredores_10k[a] = corredores_10k[a + 1]
            corredores_10k[a + 1] = temp
print(corredores_10k)
