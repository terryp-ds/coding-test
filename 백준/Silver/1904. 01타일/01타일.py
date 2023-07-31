n = int(input())

dic = {1:1, 2:2}

for i in range(1, n+1):
    if i not in dic:
        dic[i] = (dic[i-1]+dic[i-2]) % 15746


print(dic[n])
