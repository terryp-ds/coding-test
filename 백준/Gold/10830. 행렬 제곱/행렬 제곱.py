from functools import reduce
import sys
input = sys.stdin.readline

def matmul(matrix1, matrix2):
    new_matrix = []

    for row in matrix1:
        new_row = []
        
        for idx, _ in enumerate(row):
            new_row.append(sum(map(lambda x,y:x*y, row, [row2[idx] for row2 in matrix2])) % 1000)

        new_matrix.append(new_row)
        
    return new_matrix


n,b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
b2 = [int(i) for i in bin(b)[2:][::-1]]
dic = {0:matrix}

if b == 1:
    for i in range(n):
        matrix[i] = list(map(lambda x: x%1000, matrix[i]))

else:
    for i in range(1, len(b2)):
        dic[i] = matmul(dic[i-1], dic[i-1])

    matrix = reduce(matmul, [dic[i] for i,j in enumerate(b2) if j])
    
for row in matrix:
    print(*row, sep=' ')
