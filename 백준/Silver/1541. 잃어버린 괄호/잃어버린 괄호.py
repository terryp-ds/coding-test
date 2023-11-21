s=[sum(map(int,x.split('+'))) for x in input().split('-')]
print(s[0]*2-sum(s))