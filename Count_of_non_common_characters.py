n1=input().lower()
n2=input().lower()
s=""
for i in n2:
    if i not in n1 and i!=" " and i not in s:
        s+=i
for j in n1:
    if j not in n2 and j not in s and j!=" ":
        s+=j
print(len(s)-1)