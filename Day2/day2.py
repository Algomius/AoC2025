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
            if n_str[:milieu] == n_str[milieu:]:
                somme = somme + n

print (somme)