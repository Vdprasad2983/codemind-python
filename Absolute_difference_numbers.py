n,m=map(int,input().split())
l=len(str(n))
first=n//(10**(l-m))
last=n%(10**(m))
print(abs(first-last))