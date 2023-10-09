x = input()
i = x.split()
occ = set()
for n in i:
    if n in occ:
        print("YES")
    else:
        print("NO")
        occ.add(n)