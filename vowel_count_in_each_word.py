def vowel(n):
    c=0
    for i in n:
        if i in "aeiou":
            c+=1
    return c
n=list(input().split())
for i in n:
    print(vowel(i),end=" ")