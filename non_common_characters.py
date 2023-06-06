n1=input().lower()
n2=input().lower()
n1=set(n1)
n2=set(n2)
n3=n1.symmetric_difference(n2)
a=[]
for i in n3:
    if i.isalpha():
        a.append(i)
        a.sort()
for i in a:
    print(i,end="")