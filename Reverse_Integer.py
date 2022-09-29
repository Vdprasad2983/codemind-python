def reverse(n):
    rev=0
    if n>=0:
        while n:
            d=n%10
            n=n//10
            rev=rev*10+d
        return rev
    else:
        n=n*(-1)
        while n:
            d=n%10
            n=n//10
            rev=rev*10+d
        return rev*(-1)
    
n=int(input())
res=reverse(n)
print(res)