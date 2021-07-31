class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand_from_middle(str, left, right):

            if not str or left > right:
                return 0

            while left >= 0 and right < len(str) and str[left] == str[right]:
                left -= 1
                right += 1

            return(right - left - 1)

        maxL = 0
        mid = None

        for i in range(len(s)):
            l1 = expand_from_middle(s, i, i)
            l2 = expand_from_middle(s, i, i + 1)
            l = max(l1, l2)

            if l > maxL:
                mid = i
                maxL = l

        if maxL % 2 != 0:
            left = mid - int(maxL/2)
            right = mid + int(maxL/2) + 1
            return(s[left:right])

        else:
            left = mid - (int(maxL/2)) + 1
            right = mid + (int(maxL/2) + 1)
            return(s[left:right])
