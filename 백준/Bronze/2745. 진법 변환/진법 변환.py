a,b=input().split()
d=dict(zip([str(i) for i in range(10)]+list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), range(36)))
print(sum([d[x]*int(b)**(len(a)-i-1) for i,x in enumerate(a)]))