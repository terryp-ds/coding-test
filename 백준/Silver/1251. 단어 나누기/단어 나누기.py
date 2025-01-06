from itertools import combinations
s=input()
a=[]
for i,j in combinations(range(len(s)-1),2):
 x,y,z=map(lambda x:x[::-1],(s[:i+1],s[i+1:j+1],s[j+1:]))
 a+=[x+y+z]
print(sorted(a)[0])