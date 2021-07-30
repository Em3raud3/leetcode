class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arry = list()

        for i in nums:
            if (i in arry):
                continue
            else:
                arry.append(i)

        nums = arry
        return len(nums)
