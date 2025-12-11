f = open("input.txt")
pos = []
cpt = 0
for ligne in f:
    ligne = ligne[:-1]
    if "S" in ligne:
        pos.append(ligne.find("S"))
    else:
        newPos = []
        for e in pos:
            if ligne[e] == "^":
                newPos.append(e-1)
                newPos.append(e+1)
                cpt += 1
            else:
                newPos.append(e)
        pos = list(set(newPos))

print(cpt)