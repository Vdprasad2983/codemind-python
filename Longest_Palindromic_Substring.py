def pal(n):
    s_l=n[::-1]
    if n==s_l:
        return True
    else:
        return False
n=input()
x=[]
for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        if pal(n[i:j]):
            x.append(n[i:j])
c=[len(i) for i in x]
m=c.index(max(c))
print(x[m])