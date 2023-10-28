import sys
input=sys.stdin.readline
class Trie():
    def __init__(self):
        self.r={}
    def add(self,s):
        c=self.r
        for n in s:
            if n not in c: c[n]={}
            c=c[n]
        c[0]=1
    def check(self,c):
        global f
        if len(c)>1 and 0 in c: f=1
        else:
            for k in c:
                if k: self.check(c[k])
for _ in range(int(input())):
    t=Trie()
    for _ in range(int(input())): t.add(input().strip())
    f=0
    t.check(t.r)
    print(['YES','NO'][f])