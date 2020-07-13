class Solution:
    def balancedStringSplit(self, s: str) -> int:
        R_num = 0
        L_num = 0
        output = 0
        for i in range(len(s)):
            if(s[i]=='R'):
                R_num += 1
            if(s[i]=='L'):
                L_num += 1
            if((R_num != 0) and (L_num != 0) and (R_num == L_num)):
                output += 1
                R_num=0
                L_num=0
        return output