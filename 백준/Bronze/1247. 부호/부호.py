import sys
f=lambda:int(sys.stdin.readline())
for i in range(3):
 s=sum([f() for _ in range(f())])
 print('0-+'[(s!=0)+(s>0)])