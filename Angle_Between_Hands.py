n=(input())
h,m=n.split(":")
a=abs((int(h)*30)-(int(m)*5.5))
if a<180:
    print(a)
else:
    print(360-a)