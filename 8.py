max = set(i + 1 for i in range(int(input())))
zadumal = input()
while zadumal != 'HELP':
    zadumal = set(int(x) for x in zadumal.split())
    
    if len(zadumal & max) > len(max) / 2:
        print('YES')
        max &= zadumal
    else:
        print('NO')
        max -= zadumal
        
    zadumal = input()
print(*sorted(max, key=int))