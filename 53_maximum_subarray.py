class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        best = [0 for i in range(len(nums))]
        best[0] = nums[0]

        for i in range(1, len(nums)):
            best[i] = max(best[i-1] + nums[i], nums[i])

        return max(best)
