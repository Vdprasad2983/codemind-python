def vowel(n):
    c=0
    for i in n:
        if i in "aeiou":
            c+=1
    return c
n=list(input().split())
l=[vowel(i) for i in n]
m=max(l)
print(l.count(m))