class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum = 0
        count = 0
        d_sum = {0:1}
        
        for num in nums:
                running_sum += num
                
                if (running_sum - k) in d_sum:
                        count += d_sum[running_sum - k]
                        
                d_sum[running_sum] = d_sum.get(running_sum, 0) + 1
        
        return count