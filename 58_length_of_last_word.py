class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s.isspace():
            s_list = s.split()
            return len(s_list[-1])

        return 0
