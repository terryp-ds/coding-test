class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted([i for i in logs if i.split()[-1].isalpha()], key=lambda x: (x.split()[1:], x.split()[0]))+[i for i in logs if i.split()[-1].isnumeric()]