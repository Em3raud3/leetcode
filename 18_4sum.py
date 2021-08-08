class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            anchor = i+1

            for x, q in enumerate(nums[anchor:]):
                left, right = anchor + 1 + x, len(nums) - 1
                while left < right:
                    foursum = a + q + nums[left] + nums[right]

                    if foursum < target:
                        left += 1

                    elif foursum > target:
                        right -= 1

                    else:
                        res.append([a, q, nums[left], nums[right]])
                        left += 1
                        while nums[left] == nums[left-1] and left < right:
                            left += 1

        res = [z for z in {tuple(x) for x in res}]

        return res
