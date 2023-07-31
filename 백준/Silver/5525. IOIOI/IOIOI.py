n = int(input())
m = int(input())
s = input().rstrip()
p = 'I'+'OI'*n
c = 0
for i in range(m-2*n):
    if s[i:].startswith(p):
        c += 1

print(c)
