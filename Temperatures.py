n=int(input())
l=list(map(int,input().split()))
x=[]
for i in range(len(l)):
    a=0
    for j in range(i+1,len(l)):
        a+=1
        if l[j]>l[i]:
            x.append(a)
            break
    else:
        x.append(0)
print(*x)