n=input()
l=len(n)
c=(sum([n[i]!=n[i+1] for i in range(l-1)])+1)//2
print(min(c,l-c))