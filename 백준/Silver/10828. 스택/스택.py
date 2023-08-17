import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.data=[]
    def push(self, x):
        self.data.append(x)
    def pop(self):
        if self.data:
            print(self.data.pop())
        else:
            print(-1)
    def size(self):
        print(len(self.data))
    def empty(self):
        print(int(len(self.data)==0))
    def top(self):
        print(self.data[-1] if self.data else -1)  

n=int(input())
c=[input().rstrip().split() for i in range(n)]
s=Stack()

for i in c:
    if len(i) == 2:
        eval(f's.push({i[1]})')
    else:
        eval(f's.{i[0]}()')