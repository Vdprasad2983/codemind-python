n=int(input())
l=list(map(int,input().split()))
s=''
for i in l:
    s+=str(i)
x=(int(s)+1)
a=str(x)
print(*(list(a)))