from collections import deque
a=deque([i for i in range(1,int(input())+1)])
while len(a)>1:
    print(a.popleft(),end=' ')
    a.append(a.popleft())
print(a[0])