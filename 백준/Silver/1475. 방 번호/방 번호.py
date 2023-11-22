from collections import Counter
c=Counter(input().replace('6','9'))
c['9']=(c['9']+1)//2
print(c.most_common()[0][1])