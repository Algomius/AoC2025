f = open("input.txt")
diese = []
for ligne in f:
    ligne = ligne[:-1]
    x, y = ligne.split(',')
    diese.append([int(x), int(y)])

maxDim = 0
for i in range(len(diese)-1):
    for j in range(i+1, len(diese)):
        carre = (abs(diese[i][0] - diese[j][0]) + 1) * (abs(diese[i][1] - diese[j][1]) + 1)
        if carre > maxDim:
            maxDim = carre

print(maxDim)