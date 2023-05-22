def reverse(n):
    return n[::-1]
n=input()
l=list(n.split(" "))
l_i=l[::-1]
for i in l_i:
    print(reverse(i),end=" ")