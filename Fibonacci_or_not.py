n=int(input())
n1,n2=0,1
n3=n1+n2
while n3<n:
    n3=n1+n2
    n1=n2
    n2=n3
if n==n3:
    print("True")
else:
    print("False")