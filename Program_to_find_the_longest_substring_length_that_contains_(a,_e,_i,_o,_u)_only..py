def all_vowel(n):
    s="aeiou"
    for i in n:
        if i not in s:
            return False
    return True
n=input()
x=[]
for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        if all_vowel(n[i:j]):
            x.append(n[i:j])
c=[len(i) for i in x]
print(max(c))