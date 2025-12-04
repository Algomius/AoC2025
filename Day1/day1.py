position = 50
cpt = 0

f = open("input.txt")
for ligne in f:
    sens = ligne[0]
    distance = int(ligne[1:])

    if sens == "L":
        position = (position - distance) % 100
    else:
        position = (position + distance) % 100
    
    if position == 0:
        cpt = cpt +1

print(cpt)