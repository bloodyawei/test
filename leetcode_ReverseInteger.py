class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        if x >= 0:
            x_int = int(x_str[::-1])
        else:
            x_int = (-1)*int(x_str[-1:0:-1])
        if (2**31 - 1) > x_int > (-(2**31)):
            return x_int
        else:
            return 0

        #x_str = str(x)
        #x_lst = list(x_str)
        #negative = False
        #if x_lst[0] == "-":
        #    negative = True
        #    x_lst.remove(x_lst[0])
        #x_lst.reverse()
        #if negative:
        #    x_lst.insert(0, "-")
        #x_str = "".join(x_lst)
        #return int(x_str)