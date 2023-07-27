from math import ceil
from collections import Counter

def solution(progresses, speeds):
    
    time = []
    
    for p,s in zip(progresses, speeds):
        
        time.append(ceil((100-p)/s))
        
    time2 = []
    
    for i,t in enumerate(time):
        
        time2.append(max(time[:i+1]))
        
    ans = []
        
    return list(Counter(time2).values())