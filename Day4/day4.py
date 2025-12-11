f = open("input.txt")
map = []
for ligne in f:
    ligne = ligne[:-1]
    ligne = "." + ligne + "."
    if not map:
        map.append("." * len(ligne))
    map.append(ligne)

map.append("." * len(map[-1]))

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

print(cptBall)

