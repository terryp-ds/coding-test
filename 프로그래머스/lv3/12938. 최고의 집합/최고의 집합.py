def solution(n, s):
    if n > s:
        return [-1]
    
    else:
        return [s//n]*(n-s%n) + [s//n+1]*(s%n)
