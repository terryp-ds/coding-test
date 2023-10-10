import sys
input=sys.stdin.readline

class Trie():
    def __init__(self):
        self.root={}
    def add(self,w):
        c=self.root
        for s in w:
            if s not in c: c[s]={}
            c=c[s]
        c[0]=1
    def check(self,w,n):
        c=self.root
        for i in range(n):
            if 0 in c and w[i:] in s: return 1
            if w[i] not in c: return 0
            c=c[w[i]]

t=Trie()
c,k=map(int,input().split())
s=set()
for _ in range(c): t.add(input().strip())
for _ in range(k): s.add(input().strip())
for _ in range(int(input())):
    w=input().strip()
    print('Yes' if t.check(w,len(w)) else 'No')
