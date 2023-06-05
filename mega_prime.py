import math
def prime(n):
    if n==1:
        return False
    s=int(math.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
def megaprime(n):
    if not prime(n):
        return False
    for i in str(n):
        if not prime(int(i)):
            return False
    return True
n=int(input())
if megaprime(n):
    print("Mega Prime")
else:
    print("Not Mega Prime")