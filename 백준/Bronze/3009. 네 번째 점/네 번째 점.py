from collections import Counter
a=[[],[]]
for _ in range(3):
 y,x=map(int,input().split())
 a[0]+=[y]
 a[1]+=[x]
a=map(lambda x:Counter(x).most_common(2)[1][0],a)
print(*a)