atletas = [['inti',24],['lauti',19],['manu',22]]

for i in range(1, len(atletas)):
    for a in range(len(atletas) - i):
        if (atletas[a][1] > atletas[a + 1][1]):
            temp = atletas[a]
            atletas[a] = atletas[a +1]
            atletas[a + 1] = temp
print(atletas)