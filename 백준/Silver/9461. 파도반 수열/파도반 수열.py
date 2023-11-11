import sys
input=sys.stdin.readline
p=[0,1,1]+[0]*98
for i in range(3,101):p[i]=p[i-2]+p[i-3]
for _ in range(int(input())):print(p[int(input())])