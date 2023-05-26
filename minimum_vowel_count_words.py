def vowel(n):
    c=0
    for i in n:
        if i in "aeiou":
            c+=1
    return c
m=list(input().split())
x=[]
for i in m:
    x.append(vowel(i))
a=(min(x))
print(x.count(a))