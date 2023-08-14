import sys
input = sys.stdin.readline

while 1:
    string = input().rstrip()

    if string == '0':
        break

    print('yes' if string == string[::-1] else 'no')
