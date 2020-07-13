class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        head = min(strs, key = len)
        for i, c in enumerate(head):
            for words in strs:
                if words[i] != c:
                    return head[:i]
        return head
        #strs.sort(key = len)
        #if not strs:
        #    return ""
        #elif(len(strs) == 1):
        #    return strs[0]
        #else:
        #    for i in range(len(strs[0])):
        #        prev = strs[0][i]
        #        for j in range(1,len(strs)):
        #            if strs[j][i] != prev:
        #                return strs[0][:i]

        #if not strs: return ""
        #s1 = min(strs)
        #s2 = max(strs)

        #for i, c in enumerate(s1):
        #    if c != s2[i]:
        #        return s1[:i]
        #return s1

        #if not strs: return ""
        #pre = min(strs, key = len)
        #for i, c in enumerate(pre):
        #    for word in strs:
        #        if word[i] != c:
        #            return pre[:i]
        #return pre