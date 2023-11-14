from itertools import combinations

def solution(nums):
    comb = combinations(nums,3)
    n = 0
    for c in comb:
        s = sum(c)
        if not s%2: continue
        for i in range(3,int(s**0.5)+1,2):
            if not s%i: break
        else: n+=1
    return n
            
            
    answer = -1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer