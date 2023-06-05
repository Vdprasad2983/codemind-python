n=int(input())
l=list(map(int,input().split()))
l=set(l)
l=sorted(l)
if n<3:
    print(l[-1])
else:
    print(l[-3])