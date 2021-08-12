from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict = defaultdict(list)

        for s in strs:
            dict[tuple(sorted(s))].append(s)

        return dict.values()