n=int(input())
l=list(map(int,input().split()))
x=l[::2]
y=l[1::2]
a=abs(sum(x)-sum(y))
if a%4==0:
    print("X")
else:
    print("Y")