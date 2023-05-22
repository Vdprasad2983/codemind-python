import math
def is_prime(n):
    if  n==1:
        return False
    s=int(math.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
n=int(input())
c=0
l=list(map(int,input().split()))
for i in l:
    if is_prime(i):
        c+=1
print(c)