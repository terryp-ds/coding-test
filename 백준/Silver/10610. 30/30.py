s=input()
if s.count('0')>0 and sum(map(int,list(s)))%3==0: print(*sorted(s)[::-1],sep='')
else: print(-1)