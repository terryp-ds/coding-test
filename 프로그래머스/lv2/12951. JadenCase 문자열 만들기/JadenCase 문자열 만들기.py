def solution(s):
    ans = []
    ans.append(s[0].upper() if s[0].isalpha() else s[0])

    for idx, letter in enumerate(s[1:]):
        if letter.isalpha():
            ans.append(letter.upper() if s[idx] == ' ' else letter.lower())
            
        else:
            ans.append(letter)
            
    return ''.join(ans)
        