from math import sqrt
def squares(a, b):
    for i in range(a, b+1):
        yield sqrt(i)

a = int(input())
b = int(input())
result = ', '.join(str(i) for i in squares(a, b))
print(result)