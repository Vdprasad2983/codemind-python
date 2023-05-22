def is_prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
c=[j for j in l if is_prime(j)]
print("%.2f"%(sum(c)/len(c)))