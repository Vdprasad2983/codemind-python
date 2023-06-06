n1=input().lower()
n2=input().lower()
s1=""
s2=""
for i in n1:
    if i!=" ":
        s1+=i
for j in n2:
    if j!=" ":
        s2+=j
s=''
for i in s2:
    if i in s1 and i not in s:
        s+=i
print(len(s))