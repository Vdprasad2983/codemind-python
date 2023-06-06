import math
def prime(n):
    if n==1:
        return False
    s=int(math.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
a=int(input())
b=int(input())
s=a+b
for i in range(1,100):
    s+=1
    if prime(s):
        print(i)
        break