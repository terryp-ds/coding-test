from collections import deque
import sys

n_case=int(input())

for i in range(n_case):
    func, len_arr, arr = [sys.stdin.readline().rstrip() for j in range(3)]
    func, len_arr, arr = deque(func), int(len_arr), deque(arr[1:-1].split(','))
    
    reverse = 0
    flag = 1
    
    if len_arr == 0:
        arr = []
        
    for letter in func:
        if letter == 'R':
            reverse = 1 - reverse
            
        else:
            if len(arr) < 1:
                flag = 0
                print("error")
                break
                
            else:
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
                    
    if flag:
        if reverse:
            arr = list(arr)[::-1]
        print('['+','.join(arr)+']')