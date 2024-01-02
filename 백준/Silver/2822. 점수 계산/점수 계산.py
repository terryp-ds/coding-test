s=sorted([(int(input()),i) for i in range(1,9)])[3:]
print(sum([x[0] for x in s]))
print(*sorted([x[1] for x in s]))