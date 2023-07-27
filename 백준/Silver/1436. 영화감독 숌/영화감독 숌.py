nums = [str(i).zfill(4) for i in range(9999)]
nums2 = []

for num in nums:
    for i in range(len(num)+1):
        nums2.append(num[:i] + '666' + num[i:])

nums2 = sorted([int(i) for i in set(nums2)])[:10000]

print(nums2[int(input())-1])