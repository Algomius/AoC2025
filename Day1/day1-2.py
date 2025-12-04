position = 50
cpt = 0

f = open("input.txt")
for ligne in f:
    sens = ligne[0]
    distance = int(ligne[1:])

    for _ in range(distance):

        if sens == "L":
            position = (position - 1) % 100
        else:
            position = (position + 1) % 100
        
        if position == 0:
            cpt = cpt +1

print(cpt)