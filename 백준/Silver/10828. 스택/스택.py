from collections import deque
import sys
class Stack:
    def __init__(self):
        self.data=deque()
    def push(self, x):
        self.data.appendleft(x)
    def pop(self):
        if self.data:
            print(self.data.popleft())
        else:
            print(-1)
    def size(self):
        print(len(self.data))
    def empty(self):
        print(int(len(self.data)==0))
    def top(self):
        print(self.data[0] if self.data else -1)
        
n=int(input())
s=Stack()
c=[sys.stdin.readline().strip().split() for i in range(n)]
for i in c:
    if len(i) == 2:
        eval(f's.push({i[1]})')
    else:
        eval(f's.{i[0]}()')