from typing import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        NumsCount = Counter(nums)
        freq = [[] for x in range(len(nums)+1)]

        for i in NumsCount:
            freq[NumsCount[i]].append(i)

        res = []

        while len(res) < k:
            if not freq[-1]:
                freq.pop()

            else:
                res.append(freq[-1].pop())

        return res