def reverse(a):
    n=a.lower()
    s=n[::-1]
    if n==s:
        return True
    else:
        return False
s=input()
c=0
lst=(list(s.split(" ")))
for i in lst:
    if reverse(i):
        c+=1
print(c)