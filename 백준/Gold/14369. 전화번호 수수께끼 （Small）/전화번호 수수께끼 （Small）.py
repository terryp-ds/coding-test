from collections import Counter
for i in range(int(input())):
 s={k:0 for k in 'ZWUXGSFHOI'}
 s.update(Counter(input()))
 d={}
 for x,y in zip(list('ZWUXG'),[0,2,4,6,8]): d[y]=s[x]
 for x,(y,z) in zip(list('SFH'),[(7,6),(5,4),(3,8)]): d[y]=s[x]-d[z]
 for x,(y,*z) in zip(list('OI'),[(1,0,2,4),(9,5,6,8)]): d[y]=s[x]-sum([d[w] for w in z])
 s=''
 for k,v in d.items(): s+=str(k)*v
 print(f"Case #{i+1}: {''.join(sorted(s))}")