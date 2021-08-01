# https://www.youtube.com/watch?v=erEHQO0xljc

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        results = set()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                results.add(total)

                if total < target:
                    left += 1

                elif total > target:
                    right -= 1

                else:
                    left += 1
                    right -= 1

        results = list(results)
        results.sort()

        looking = [abs(x - target) for x in results]
        answer = min(looking)
        index = looking.index(answer)

        return(results[index])
