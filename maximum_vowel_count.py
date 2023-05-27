def vowel(n):
    c=0
    for i in n:
        if i in "aeiou":
            c+=1
    return c
n=list(input().split())
l=[]
for i in n:
    l.append(vowel(i))
print(max(l))