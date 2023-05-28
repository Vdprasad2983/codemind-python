def vowel(n):
    if n in "aeiou":
        return True
    return False
def fun(n):
    l=list(n)
    c=0
    for i in range(len(l)):
        if (vowel(l[i]) and not vowel(l[-i-1])) :
            c+=1
    return c
n=input()
l=list(n.split(" "))
l2=[]
for i in range(len(l)):
    l2.append(fun(l[i]))
print(sum(l2))