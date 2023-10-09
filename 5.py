n, m = input().split()
anna = set()
borya = set()
for i in range(int(n)):
    anna.add(int(input()))
for i in range(int(m)):
    borya.add(int(input()))
print(len(anna&borya))
print(*sorted(anna&borya))
print(len(anna-borya))
print(*sorted(anna-borya))
print(len(borya-anna))
print(*sorted(borya-anna))