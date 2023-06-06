import math
def prime(n):
    if n==1:
        return False
    s=int(math.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
n=int(input())
p=[i for i in range(1,n+1) if n%i==0]
n_p=[i for i in p if not prime(i)]
print(len(n_p))