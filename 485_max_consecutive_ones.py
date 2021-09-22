class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        longest, current = 0, 0
        
        for i in nums:
            if i == 1:
                current +=1
                longest = max(current, longest)
            else:
                current = 0
        
        return longest