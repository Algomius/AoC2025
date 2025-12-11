def remove(map):
    cptBall = 0
    for i in range(1, len(map)-1):
        for j in range(1, len(map[0])- 1):
            if map[i][j] == "@":
                cpt = 0
                for k in (-1, 0, +1):
                    for l in (-1, 0, +1):
                        if (k != 0 or l != 0) and map[i+k][j+l] == "@":
                            cpt += 1
                if cpt < 4:
                    cptBall += 1
                    map[i][j] = "."
    return cptBall

f = open("input.txt")
map = []
for ligne in f:
    ligne = ligne[:-1]
    ligne = list("." + ligne + ".")
    if not map:
        map.append(list("." * len(ligne)))
    map.append(ligne)

map.append(list("." * len(map[-1])))

cpt= remove(map)
cptBall = cpt
while cpt > 0:
    cpt= remove(map)
    cptBall += cpt 

print(cptBall)

