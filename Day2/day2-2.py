def estInvalide(n):
    for l in range(1, (len(n) // 2) + 1):
        pattern = n[:l]
        test = True
        for i in range(l, len(n), +l):
            if pattern != n[i:i+l]:
                test = False
        if test:
            return True
    return False

somme = 0
f = open("input.txt")
for ligne in f:
    ligne = ligne[:-1]
    intervalle = ligne.split(",")
    for i in intervalle:
        borneMin, borneMax = i.split("-")
        for n in range(int(borneMin), int(borneMax)+1):
            n_str = str(n)
            milieu = len(n_str) // 2
            if estInvalide(n_str):
                somme = somme + n

print (somme)