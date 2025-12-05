somme = 0
f = open("input.txt")
for ligne in f:
    ligne = ligne[:-1]
    maxJolt = ""
    while ligne:
        if maxJolt == "":
            maxJolt += ligne[0]
        elif maxJolt[-1] >= ligne[0]:
            if len(maxJolt) < 12:
                maxJolt += ligne[0]
        else:
            while maxJolt and ligne[0] > maxJolt[-1] and len(maxJolt) + len(ligne) > 12:
                maxJolt = maxJolt[:-1]

            if len(maxJolt) + len(ligne) == 12:
                maxJolt += ligne
                ligne = ""
            else:
                maxJolt += ligne[0]
        ligne = ligne[1:] 
    somme = somme + int(maxJolt)

print(somme)