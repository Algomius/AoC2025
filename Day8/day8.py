def distance(l1, l2):
    minDist = float('inf')
    x1, y1, z1, g1 = l1
    x2, y2, z2, g2 = l2
    return pow(x1-x2,2) + pow(y1-y2,2) + pow(z1-z2,2)

f = open("input.txt")
conn = []
l = []
cpt = 0
ensemble = []
for ligne in f:
    ligne = ligne[:-1]
    x, y, z = ligne.split(',')
    conn.append([int(x), int(y), int(z), cpt])
    l.append(1)
    cpt += 1
    ensemble.append(1)

distances = []
for i in range(len(conn)-1):
    for j in range(i+1, len(conn)):
        d = distance(conn[i], conn[j])
        distances.append([d, [i, j]])

distances.sort()
n = 0
while n <1000:
    d, ind = distances[n]
    premier = conn[ind[0]][3]
    second = conn[ind[1]][3]
    if premier != second:
        for i in range(len(conn)):
            if conn[i][3] == second:
                conn[i][3] = premier
                ensemble[second] -= 1
                ensemble[premier] += 1
    n += 1

ensemble.sort(reverse=True)

mult = 1
for i in range(3):
    mult *= ensemble[i]

print(mult)

