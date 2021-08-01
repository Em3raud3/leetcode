class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = list(str(x))
        x_rev = list(str(x))
        x_rev.reverse()
        return x_rev == x_str
