class Solution:
    def maxArea(self, height: List[int]) -> int:

        if not height or len(height) == 1:
            return 0

        left = 0
        right = len(height) - 1

        most = 0
        while left < right:
            for i in range(len(height)):
                l = min(height[left], height[right])
                w = right - left
                v = l*w
                most = max(most, v)

                if height[left] < height[right]:
                    left += 1

                else:
                    right -= 1
        return most
