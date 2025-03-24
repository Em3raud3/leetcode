class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        checked_nums = set()
        res = 0
        current_longest = 0

        for num in nums:
            if num in checked_nums:
                continue
            else:
                checked_nums.add(num)
                current_longest = 1
                left = num - 1
                right = num + 1

                while left in set_nums:
                    checked_nums.add(left)
                    left -= 1
                    current_longest += 1

                while right in set_nums:
                    checked_nums.add(right)
                    right += 1
                    current_longest += 1

                res = max(res, current_longest)

        return res