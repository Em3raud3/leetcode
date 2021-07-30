class Solution:
    def climbStairs(self, n: int) -> int:
        if (n == 1):
            return 1

        dp = [0 for x in range(int)]
