def pal(n):
    s=str(n)
    s_l=s[::-1]
    if s==s_l:
        return True
    else:
        return False
t=int(input())
for i in range(t):
    n=int(input())
    print(pal(n))