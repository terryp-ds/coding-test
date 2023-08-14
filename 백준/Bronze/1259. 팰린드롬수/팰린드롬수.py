import sys
while 1:
    s=sys.stdin.readline().strip()
    if s=='0':
        break
    if s==s[::-1]:
        print('yes')
    else:
        print('no')