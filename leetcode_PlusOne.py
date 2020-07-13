class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #str_list = ""
        #for i in range(len(digits)):
        #    str_list += str(digits[i])
        #int_res = int(str_list)
        str_list = [str(x) for x in digits]
        int_res = int("".join(str_list))
        int_res += 1
        return [int(x) for x in str(int_res)]