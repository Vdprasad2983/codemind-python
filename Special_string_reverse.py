n=input()
l=list(n)
s=[]
for i in range(len(l)):
    if l[i].isalpha():
        s.append(l[i])
        l[i]="*"
s_l=s[::-1]
a=0
for j in range(len(l)):
    if l[j]=="*":
        l[j]=s_l[a]
        a+=1
for k in l:
    print(k,end="")