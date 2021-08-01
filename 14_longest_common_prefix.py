class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        length = min(len(l) for l in strs)
        counter = 0

        for i in range(length):
            checker = set()

            for word in strs:
                checker.add(word[i])

            if len(checker) == 1:
                counter += 1

            else:
                break

        return strs[0][0:counter]
