import sys
input=sys.stdin.readline

class Trie:
    def __init__(self):
        self.r={}

    def add(self,f):
        c=self.r
        for s in f:
            if s not in c: c[s]={}
            c=c[s]
        c[0]=1
	
    def travel(self,c,d):
        if 0 in c: return
        for s in sorted(c):
            print("--"*d+s)
            self.travel(c[s],d+1)

t=Trie()
for i in range(int(input())): t.add(input().split()[1:])
t.travel(t.r,0)