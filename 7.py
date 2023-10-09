n = int(input())
zadumal = set()
a = set()
while True:
    for i in range(1):
        a.update(input().split())
    if 'HELP' in a:
        zadumal.remove('YES')
        print(' '.join(sorted(zadumal)))
        break
    if 'YES' in a:
        if zadumal == set():
            zadumal |= a
        elif zadumal != a:
            zadumal = (zadumal & a)
        a = set()
    elif 'NO' in a:
        zadumal -= a
        a = set()