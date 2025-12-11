f = open("input.txt")
last = []
n = []
for ligne in f:
    ligne = ligne[:-1]
    if last:
        last = [int(x) for x in last]
        n.append(last)
    last = ligne.split(" ")
    last = [x for x in last if x != '']

s = 0
for i in range(len(n[0])):
    result = 0
    if last[i] == '*':
        result = 1
        for j in range(len(n)):
            result *= n[j][i]
    else: 
        result = 0
        for j in range(len(n)):
            result += n[j][i]
    s += result
    
print(s)