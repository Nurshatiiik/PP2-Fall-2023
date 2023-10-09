A = input()
B = input()
list1 = list(map(int, A.split()))
list2 = list(map(int, B.split()))
intersection = sorted(set(list1) & set(list2))
if intersection:
    print()
    for i in intersection:
        print(i)
else:
    print()