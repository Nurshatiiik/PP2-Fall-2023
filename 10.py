n,k = map(int,input().split())
cnt = set()
for i in range(k):
    a,b = map(int,input().split())
    while a <= n:
        if 0 < a % 7 < 6:
            cnt.add(a)
        a += b
print(len(cnt))