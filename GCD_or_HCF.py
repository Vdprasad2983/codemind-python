a,b=map(int,input().split())
x=min(a,b)
for i in range(1,x+1):
    if ((a%i==0) and (b%i==0)):
        gcd=i
print(gcd)