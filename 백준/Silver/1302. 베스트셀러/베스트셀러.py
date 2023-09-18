import sys
input=sys.stdin.readline
d={}
for _ in range(int(input())):
    w=input().strip()
    if w not in d:d[w]=0
    d[w]+=1
print(sorted(sorted(d.items(),key=lambda x: x[0]),key=lambda x:x[1],reverse=True)[0][0])