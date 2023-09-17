a=int(input())
b=int(input())
c=int(input())
if a%2==0:
    a2=a//2
else:
    a2=(a//2)+1
if b%2==0:
    b2=b//2
else:
    b2=(b//2)+1
if c%2==0:
    c2=c//2
else:
    c2=(c//2)+1

print(a2+b2+c2)