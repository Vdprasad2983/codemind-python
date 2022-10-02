x=int(input())
n=x**2
rev1=0
while x!=0:
    d=x%10
    rev1=rev1*10+d
    x=x//10
m=rev1**2
rev2=0
while m!=0:
    d=m%10
    rev2=rev2*10+d
    m = m//10
if n==rev2:
    print("True")
else:
    print("False")