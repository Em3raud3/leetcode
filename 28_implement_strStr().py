class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not (needle in haystack):
            return -1

        if not needle:
            return 0

        if (needle in haystack):
            return haystack.index(needle[0])
