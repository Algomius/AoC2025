f = open("input.txt")
inter = True
intervalles = []
cpt = 0
for ligne in f:
    ligne = ligne[:-1]
    if ligne == "":
        inter = False
    elif inter:
        borneMin, borneMax = ligne.split('-')
        intervalles.append((int(borneMin), int(borneMax)))
    else:
        ele = int(ligne)
        isInInter = False
        for borneMin, borneMax in intervalles:
            if borneMin <= ele and ele <= borneMax:
                isInInter = True
        if isInInter:
            cpt += 1

print(cpt)

