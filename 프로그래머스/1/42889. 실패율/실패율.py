from collections import Counter

def solution(N, stages):
    c = Counter(stages)
    d = []
    t = len(stages)
    for i in range(1,N+1):
        if not t: 
            d.append((1,i))
            continue
        if i not in c: f = 0
        else: f = c[i]
        d.append((1-f/t,i))
        t-=f

    return [x[1] for x in sorted(d)]