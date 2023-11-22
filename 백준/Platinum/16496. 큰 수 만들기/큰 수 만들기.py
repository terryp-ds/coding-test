input()
a=input().split()
z=''.join([i[1] for i in sorted(zip([i*(10//len(i))+i[:10%len(i)] for i in a],a),reverse=True)])
print([0,z][int(z)>0])