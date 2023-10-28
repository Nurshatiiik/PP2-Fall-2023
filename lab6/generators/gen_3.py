def numbers(n):
    for i in range(1, n+1):
        if i % 3 == 0 or i %4 == 0:
            yield i

n = int(input())
result = ', '.join(str(i) for i in numbers(n))
print(result)