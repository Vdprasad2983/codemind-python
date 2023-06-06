n1=input().lower()
n2=input().lower()
s=""
for i in n1:
    if i not in n2 and i not in s and i!=" ":
        s+=i
for j in n2:
    if j not in n1 and j not in s and j!=" ":
        s+=j
b=[]
for i in s:
    if i.isalpha():
        b.append(i)
        b.sort()
for i in b:
    print(i,end="")