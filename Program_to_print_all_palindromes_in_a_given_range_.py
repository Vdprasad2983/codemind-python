def pal(n):
    s=str(n)
    s_l=s[::-1]
    if s==s_l:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if pal(i):
        print(i,end=" ")