n=input()
l=list(n)
x=[]
for i in range(len(l)):
    if l[i].isalpha():
        x.append(l[i])
        l[i]="*"
x.sort()
a=0
for j in range(len(l)):
    if l[j]=='*':
        l[j]=x[a]
        a+=1
print(''.join(l))