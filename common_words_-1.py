n1=list((input().lower()).split())
n2=list((input().lower()).split())
c=0
for i in n2:
    if i in n1:
        c+=1
print(c)