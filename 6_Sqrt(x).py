class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        if x == 0:
            return 0

        if x == 1:
            return 1
        for i in range(x + 1):
            num = i*i
            if num <= x:
                ans = i

            else:
                return ans
