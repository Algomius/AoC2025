f = open("input.txt")
map = []
for ligne in f:
    ligne = ligne[:-1]
    map.append(ligne)

s = 0
op = ""
result = 0
for i in range(len(map[0])):
    if map[-1][i] == "*":
        s += result
        op = "*"
        st = ""
        for j in range(len(map)-1):
            if map[j][i] != " ":
                st += map[j][i]
        result = int(st)
    elif map[-1][i] == "+":
        s += result
        op = "+"
        st = ""
        for j in range(len(map)-1):
            if map[j][i] != " ":
                st += map[j][i]
        result = int(st)
    else:
        st = ""
        for j in range(len(map)-1):
            if map[j][i] != " ":
                st += map[j][i]
        if st:
            if op == "*":
                result *= int(st)
            else:
                result += int(st)

s += result  
print(s)