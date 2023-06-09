a=int(input())
b=int(input())
l=[i for i in range(a,b+1)]
s=[]
for i in range(len(l)):
    for j in range(i+1,len(l)+1):
        s.append(sum(l[i:j]))
c=0
for i in s:
    if i%2!=0:
        c+=1
print(c)