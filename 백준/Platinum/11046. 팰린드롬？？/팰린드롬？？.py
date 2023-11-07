import sys
input=sys.stdin.readline
t=[0]*(2*int(input())+1)
t[1::2]=input().strip().split()
n=len(t)
a=[0]*n 
r,p=0,0
for i in range(n):
    if i<=r:a[i]=min(a[2*p-i],r-i)
    while i+a[i]+1<n and t[i-a[i]-1]==t[i+a[i]+1]:a[i]+=1
    if r<i+a[i]:r=i+a[i];p=i
for _ in range(int(input())): 
    s,e=map(int,input().split())
    print((a[s+e-1]>=e-s)+0)