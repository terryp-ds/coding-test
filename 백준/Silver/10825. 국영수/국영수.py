import sys
input=sys.stdin.readline
n=int(input())
a=[]
for _ in range(n):
 x,*y=input().strip().split()
 a+=[[x]+[*map(int,y)]]
a=sorted(sorted(sorted(sorted(a,key=lambda x:x[0]),key=lambda x:x[3],reverse=True),key=lambda x:x[2]),key=lambda x:x[1],reverse=True)
for x in a:print(x[0])