from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if(len(s)==1):
            return 0
        dic = defaultdict(int)
        for k in s:
            dic[k] += 1
        for key, value in dic.items():
            if dic[key] == 1:
                return s.index(key)
        return -1

