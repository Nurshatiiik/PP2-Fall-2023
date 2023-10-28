def square_gen(N):
    for num in range(1, N + 1):
        yield num ** 2

N=int(input())
squares = square_gen(N)
for square in squares:
    print(square)
