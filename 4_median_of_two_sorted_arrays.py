class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        final = list()

        while nums1 or nums2:
            if nums1 and nums2:
                if nums1[0] <= nums2[0]:
                    final.append(nums1.pop(0))

                else:
                    final.append(nums2.pop(0))

            elif nums1:
                final.extend(nums1)
                nums1.clear()

            else:
                final.extend(nums2)
                nums2.clear()

        length = len(final)
        if length % 2 != 0:
            return float(final[int(length/2)])

        else:
            return (final[int(length/2)] + final[int(length/2) - 1])/2
