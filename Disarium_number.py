a=int(input())
n=a
s=len(str(a))
c=0
for i in range(1,len(str(a))+1):
    d=n%10
    c+=d**s
    n=n//10
    s-=1
if c==a:
    print("True")
else:
    print("False")