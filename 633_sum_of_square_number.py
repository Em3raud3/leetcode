import math 
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        num_set = set()
        num = 0

        while num**2 <= c:
            num_set.add(num)
            if math.sqrt(c - num**2) % 1 == 0:
                return True
            num += 1

        return False
