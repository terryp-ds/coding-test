def solution(answers):
    n=len(answers)
    pat = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    answer = [sum([p[i%len(p)]==answers[i] for i in range(n)]) for p in pat]
    return [i+1 for i in range(3) if answer[i]==max(answer)]