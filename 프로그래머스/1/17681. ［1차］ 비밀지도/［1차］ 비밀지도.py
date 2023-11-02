def solution(n, arr1, arr2):
    return [str(bin(i|j))[2:].zfill(n).replace('0',' ').replace('1','#') for i,j in zip(arr1, arr2)]