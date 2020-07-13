from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for s_key in s:
            s_dict[s_key] += 1
        for t_key in t:
            t_dict[t_key] += 1
        if s_dict == t_dict:
            return True
        else:
            return False