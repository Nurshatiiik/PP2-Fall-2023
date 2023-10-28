def down(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
result = ', '.join(str(i) for i in down(n))
print(result)
