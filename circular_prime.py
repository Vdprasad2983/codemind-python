import math
def prime(n):
    if n==1:
        return False
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
n=int(input())
temp=n
rev=0
while n:
    d=n%10
    n//=10
    rev=rev*10+d
if prime(temp) and prime(rev):
    print("circular prime")
elif prime(temp):
    print("prime but not a circular prime")
else:
    print("not prime")