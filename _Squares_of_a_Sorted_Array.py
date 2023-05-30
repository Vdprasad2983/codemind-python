n=int(input())
l=list(map(int,input().split()))
a=[abs((l[i])**2) for i in range(len(l))]
print(*(sorted(a)))