def prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
np=1
p=1
for i in l:
    if prime(i):
        p*=i
    else:
        np*=i
print(abs(np-p))