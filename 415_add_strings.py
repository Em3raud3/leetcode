import itertools


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        num1, num2 = 0 if num1.isspace() else num1, 0 if num2.isspace() else num2
        num1, num2 = list(num1), list(num2)
        num1.reverse()
        num2.reverse()

        carry = 0

        res = list()

        for x, y in itertools.zip_longest(num1, num2):
            a, b = x if x else 0, y if y else 0
            c = (int(a) + int(b)) + carry
            carry = c//10
            res.append(c % 10)

        if carry > 0:
            res.append(carry)

        res.reverse()
        ans = ""

        for i in res:
            ans += str(i)
        return ans
