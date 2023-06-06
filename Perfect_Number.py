n=int(input())
d=[]
for i in range(1,n):
    if n%i==0:
        d.append(i)
if n==sum(d):
    print(True)
else:
    print(False)