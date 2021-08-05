class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]

        for n in nums:
            tmp = []
            for l in ans:
                tmp.append(l + [n])
            ans.extend(tmp)

        return [l for l in set([tuple(x) for x in ans])]
