def reverse(n):
    return n[::-1]
n=input()
l=list(n.split(" "))
for i in l:
    print(reverse(i),end= ' ')