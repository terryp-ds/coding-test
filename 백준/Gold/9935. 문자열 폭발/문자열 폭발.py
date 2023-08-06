string = input()
pattern = input()

stack = []
length = len(pattern)
c = 0

for i in range(len(string)):
    letter = string[i]
    stack.append(letter)
    if len(stack) >= length:
        if ''.join(stack[-length:]) == pattern:
            for _ in range(length):
                stack.pop()

print(''.join(stack) if stack else 'FRULA')
