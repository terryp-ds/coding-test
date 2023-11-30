from collections import deque
n,k=map(int,input().split())
q=deque([str(i) for i in range(1,n+1)])
p=[]
while q:
    q.rotate(-k+1)
    p+=[q.popleft()]
print('<'+', '.join(p)+'>')