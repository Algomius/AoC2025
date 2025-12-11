f = open("input.txt")
intervalles = []
for ligne in f:
    ligne = ligne[:-1]
    if ligne == "":
        break
    else:
        borneMin, borneMax = ligne.split('-')
        intervalles.append([int(borneMin), int(borneMax)])

intervalles.sort()

i = 0

while i < len(intervalles)-1:
    if intervalles[i+1][0] <= intervalles[i][1]:
        intervalles[i][1] = max(intervalles[i+1][1], intervalles[i][1])
        del intervalles[i+1]
    else :
        i += 1

cpt = 0
for borneMin, borneMax in intervalles:
    cpt += borneMax - borneMin + 1

print(cpt)
