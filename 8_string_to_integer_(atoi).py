class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.lstrip()
        polarity = 0

        if len(s) == 0:
            return 0

        if len(s) == 1 and (not s[0].isdigit()):
            return 0

        #! Checks for positive or negative sign at the start
        if s[0] == "-":
            polarity = -1
            s = s[1:]

        elif s[0] == "+":
            polarity = 1
            s = s[1:]

        else:
            polarity = 1

        #! Remove leading 0's

        while s[0] == "0":
            if len(s) > 1:
                s = s[1:]

            else:
                return 0

        #! Check if leading letter is int()
        if not s[0].isdigit():
            return 0

        num = ""

        for i in s:
            if i.isdigit():
                num += i
            else:
                break

        num = int(num)

        num = num*polarity

        if num < -2**31:
            num = -2**31

        if num > 2**31 - 1:
            num = 2**31 - 1

        return num
