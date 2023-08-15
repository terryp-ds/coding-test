def solution(n, lost, reserve):
    lost, reserve = sorted(set(lost)-set(reserve)), sorted(set(reserve)-set(lost))
    
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)

        elif i+1 in lost:
            lost.remove(i+1)
            
    return n - len(lost)