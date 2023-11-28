s = [input() for i in range(5)]
m = max([len(i) for i in s])
s = [i.ljust(m,' ') for i in s]
print(''.join(''.join([''.join([i[j] for i in s]) for j in range(m)]).split()))