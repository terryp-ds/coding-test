from collections import Counter
c=sorted(Counter(input().upper()).items(), key=lambda x: x[1])
if len(c)==1 or c[-1][1]!=c[-2][1]: print(c[-1][0])
else: print('?')