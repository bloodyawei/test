class Solution:
    def myAtoi(self, str: str) -> int:

        str = str.strip()
        try:
            res = re.search('(^[\+\-]?\d+)', str).group()
            res = int(res)
            res = res if res <= 2147483647 else 2147483647
            res = res if res >= -2147483648 else -2147483648
        except:
            res = 0
        return res

        #new_str = str.lstrip()
        #output_str = ""
        #if len(new_str) == 0:
        #    return 0
        #if new_str[0].isnumeric():
        #    for s in new_str:
        #        if s.isnumeric():
        #            output_str += s
        #        else:
        #            break
        #elif new_str[0] == "-":
        #    output_str += "-"
        #    for i in range(1, len(new_str)):
        #        if new_str[i].isnumeric():
        #            output_str += new_str[i]
        #        else:
        #            break
        #else:
        #    return 0

        #if not output_str.isdigit():
        #    return 0
        #else:
        #    output_int = int(output_str)
        #    if output_int > (2**31 - 1):
        #        return (2**31 - 1)
        #    elif output_int < (-(2**31)):
        #        return (-(2**31))
        #    else:
        #        return output_int
