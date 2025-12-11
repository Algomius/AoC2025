def timeLines(posY, posX, map):
    if (posY, posX) in d.keys():
        return d[(posY, posX)]
    if posY == len(map)-1:
        d[(posY, posX)] = 1
        return 1
    if map[posY][posX] == "^":
        cpt = timeLines(posY, posX-1, map)
        cpt += timeLines(posY, posX+1, map)
        d[(posY, posX)] = cpt
        return cpt
    else:
        decal = 0
        while map[posY + decal][posX] != "^" and posY+decal < len(map)-1:
            decal += 1
        cpt = timeLines(posY+1, posX, map)
        d[(posY, posX)] = cpt
        return cpt
d = {}
f = open("input.txt")
cpt = 0
map = []
posS = -1
for ligne in f:
    ligne = ligne[:-1]
    if "S" in ligne:
        posS = ligne.find("S")
        map.append(list(ligne))
    if "^" in ligne:
        map.append(list(ligne))

map.append("." * len(map[0]))
print(timeLines(0, posS, map))