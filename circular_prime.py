import math
def prime(n):
    if n==1:
        return False
    s=int(math.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
def reverse(n):
    s=str(n)
    s_l=s[::-1]
    return int(s_l)
n=int(input())
if prime(n):
    if prime(reverse(n)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")