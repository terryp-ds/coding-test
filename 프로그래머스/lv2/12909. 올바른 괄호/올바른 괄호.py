from collections import deque

def solution(s):
    
    queue = deque(s)
    stack = []
    
    while queue:
        
        bracket = queue.popleft()
        
        if bracket == '(':
            stack.append('(')
            
        else:
            if stack:
                stack.pop()
            else:
                return False
        
    return False if stack else True