import sys

n = int(input())
num_list = [0]*10000

for _ in range(n):
    num_list[int(sys.stdin.readline().strip())-1]+= 1
    
for i in range(10000):
    if num_list[i] != 0:
        for _ in range(num_list[i]):
            print(i+1)