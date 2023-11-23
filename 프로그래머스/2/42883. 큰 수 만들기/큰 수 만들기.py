def solution(number, k):
    i=0
    while k and i<len(number)-1:
        if i>=0 and number[i]<number[i+1]:
            number = number[:i]+number[i+1:]
            k-=1
            i-=1
        else: i+=1
    if k>0: number=number[:len(number)-k]
    return number
