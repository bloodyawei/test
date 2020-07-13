class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        output = 0
        for j in range(len(J)):
            for s in range(len(S)):
                if J[j] == S[s]:
                    output += 1
        return output