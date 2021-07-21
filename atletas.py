topus = [["Mike",20],["Lucas",23],["Nacho",20],["Inti",25]]
auxmayor= topus[0]

for i in topus:
     if i[1] > auxmayor[1]:
         auxmayor = i
        
print(auxmayor)