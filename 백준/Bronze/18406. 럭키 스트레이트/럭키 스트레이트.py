n=input()
l,r=n[:len(n)//2],n[len(n)//2:]
print(['READY','LUCKY'][sum(map(int,l))==sum(map(int,r))])