class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s.isspace():

            s = list(s)
            longest = 0

            for i in range(len(s)):
                unique = set()
                for j in range(i, len(s)):
                    if not s[j] in unique:
                        unique.add(s[j])
                        longest = max(longest, len(unique))
                    else:
                        break

                if j == len(s) - 1:
                    break

            return(longest)

        return 1
