def rep(n):
    l=len(n)
    s=''
    for i in n.lower():
        if i not in s:
            s+=i
    if len(s)==l:
        return True
    else:
        return False
n=input()
x=[]
for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        if rep(n[i:j]) and len(n[i:j])>2:
            x.append(n[i:j])
if len(x)!=0:
    c=[len(i) for i in x]
    m=c.index(max(c))
    print(x[m])
else:
    print(-1)