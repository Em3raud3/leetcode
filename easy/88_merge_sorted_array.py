class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        while len(nums1) > m:
            nums1.pop()

        x = nums2[0:n]
        nums1.extend(x)
        nums1.sort()
