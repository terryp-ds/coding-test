import sys
input=sys.stdin.readline
n=int(input())
a=[*map(int,input().split())]
d=[[0]*n for _ in range(n)]
for i in range(n-1,-1,-1):
 for j in range(i,n):
  if a[i]==a[j] and (i+2>j or d[i+1][j-1]):d[i][j]=1
for _ in range(int(input())):
 s,e=map(int,input().split())
 print(d[s-1][e-1])