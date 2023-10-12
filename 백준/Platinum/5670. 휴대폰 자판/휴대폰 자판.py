import sys
input=sys.stdin.readline
class Trie():
    def __init__(self):
        self.r={1:0}
    def add(self,w):
        c=self.r
        for s in w:
            if s not in c:
                c[s]={1:0}
            c[1]+=1
            c=c[s]
        c[0]=1
    def travel(self,c):
        global k
        for s in c:
            if s==1: k+=c[s] if not k or len(c)>2 else 0
            elif s: self.travel(c[s])
        if 0 in c: return
while 1:
    try: n=int(input())
    except: break
    t=Trie()
    for _ in range(n): t.add(input().strip())
    k=0
    t.travel(t.r)
    print(f'{round(k/n,2):.2f}')