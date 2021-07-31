class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand_from_middle(s, left, right):

            if not s or left > right:
                return 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left + 1

        if not s or len(s) < 1:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            len1 = expand_from_middle(s, i, i)
            len2 = expand_from_middle(s, i, i+1)
            len3 = max(len1, len2)
            if len3 > end - start:
                start = i - ((len3 - 1)/2)
                end = i + (len3/2)

        return s[start: (end + 1)]
