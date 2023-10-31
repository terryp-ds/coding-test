from collections import Counter
s=input().upper()
c=Counter(s)
c=sorted(c.items(), key=lambda x: x[1])
if len(c)==1 or c[-1][1] != c[-2][1]:
    print(c[-1][0])
else:
    print('?')