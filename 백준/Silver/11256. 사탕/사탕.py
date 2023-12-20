import sys
input=sys.stdin.readline
for _ in range(int(input())):
 j,n=map(int,input().split())
 i,s=0,0
 a=[[*map(int,input().split())] for _ in range(n)]
 a=sorted([x[0]*x[1] for x in a],reverse=True)
 while s<j:
  s+=a[i]
  i+=1
 print(i)