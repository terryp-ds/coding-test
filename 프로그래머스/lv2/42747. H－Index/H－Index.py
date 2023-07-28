from collections import Counter

def solution(citations):
    total = len(citations)
    citations = sorted(citations, reverse=True)
    max_h,h = 0,0
    
    while citations:
        if citations[-1] < h:
            citations.pop()
            
        else:
            if (len(citations) >= h) and (total - len(citations) <= h):
                max_h = h
                h += 1
            else:
                break
            
            
    return max_h
        