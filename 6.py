n = int(input())
count = set()
for i in range(n):
    s1 = input().strip()
    words = s1.split()
    for slovo in words:
        count.add(slovo)
print(len(count))