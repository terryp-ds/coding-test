_=input()
a=input().split()
s=[*map(lambda x:sum([int(i)//x[0]+1 for i in a])*x[1],[(30,10),(60,15)])]
i=(s[1]<s[0])+(s[1]<=s[0])
print(['Y','Y M','M'][i],(s+[s[1]])[i])