from functools import reduce

def multiply(n):
    res = reduce(lambda x, y: x * y, n)
    return res

x = input()
arr = [int(n) for n in x.split()]

if arr:
    res = multiply(arr)
    print(f"{res}")
else:
    print(0)