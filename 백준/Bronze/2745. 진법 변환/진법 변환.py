n,b=input().split()
d=dict(zip(list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'),range(36)))
print(sum([d[x]*int(b)**(len(n)-i-1) for i,x in enumerate(n)]))