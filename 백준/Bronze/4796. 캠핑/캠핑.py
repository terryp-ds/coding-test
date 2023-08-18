import sys
input = sys.stdin.readline
i = 1

while 1:
    l,p,v = map(int, input().split())

    if not l:
        break

    print(f'Case {i}: {l*(v//p)+min(l,v%p)}')
    i += 1
