def pal(n):
    s=str(n)
    s_l=s[::-1]
    return int(s_l)
n=int(input())
for i in range(n):
    n=n+pal(n)
    if n==pal(n):
        print(n)
        break
