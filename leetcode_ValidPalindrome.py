class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        new_s = ""
        for s_char in s:
            if(s_char.isalnum() ):
                new_s += s_char.lower()
        new_s_list = list(new_s)
        new_s_list_ = copy.deepcopy(new_s_list)
        new_s_list_.reverse()
        if new_s_list == new_s_list_:
            return True
        else:
            return False