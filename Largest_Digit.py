n=int(input())
c=0
while n!=0:
    d=n%10
    if d>c:
        c=d
    n//=10
print(c)
    