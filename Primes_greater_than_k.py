def is_prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for j in l:
    if j>=k and is_prime(j):
        c+=1
print(c)