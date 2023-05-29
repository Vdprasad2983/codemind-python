n=int(input())
l=list(map(int,input().split()))
e=l[::2]
o=l[1::2]
x=(abs(sum(e)-sum(o)))
if x==0:
    print("YES")
else:
    print("NO")