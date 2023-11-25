s=input().replace('XXXX','AAAA').replace('XX','BB')
print([s,-1][s.count('X')>0])