def solution(s):

    s = list(eval(s[1:-1]))

    if len(s) == 1:

        return s

    else:
        s = sorted(s, key=len)

        ans = []
        
        for item in s:
            diff = item.difference(set(ans))
            ans.append(list(diff)[0])
        
        return ans
