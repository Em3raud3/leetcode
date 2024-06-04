class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for index, i in enumerate(nums):

            result = []
            result.append(index)

            pair = target - i

            if pair in nums:

                if pair == i and nums.count(i) == 1:
                    continue

                elif pair == i and nums.count(i) > 1:
                    result.append(nums.index(pair, index + 1))
                    return result

                else:
                    result.append(nums.index(pair))
                    return result
