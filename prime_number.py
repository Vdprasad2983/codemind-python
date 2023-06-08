import math
def prime(n):
    if n==1:
        return "not a prime"
    s=int(math.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return "not a prime"
    return "prime"
n=int(input())
print(prime(n))