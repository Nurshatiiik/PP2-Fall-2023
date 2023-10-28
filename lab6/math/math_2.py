def area_of_trapezoid(a, b, h):
    S = ((a+b)/2)*h
    print("Expected Output:", S)
h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
area_of_trapezoid(a, b, h)