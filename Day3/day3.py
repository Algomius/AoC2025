somme = 0
f = open("input.txt")
for ligne in f:
    ligne = ligne[:-1]
    maxJolt = 0
    for i in range(0, len(ligne)-1):
        for j in range(i+1, len(ligne)):
            if maxJolt < int(ligne[i] + ligne[j]):
                maxJolt = int(ligne[i] + ligne[j])
    somme = somme + maxJolt

print(somme)