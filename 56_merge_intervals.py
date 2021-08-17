class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) <= 1:
            return intervals

        def is_interval(a:list, b:list):



            if (a[0] <= b[0] <= a[1]) or (a[0] <= b[1] <= a[1]) or (b[0] <= a[0] <= b[1]) or (b[0] <= a[1] <= b[1]):
            # return [min(a[0],b[0]), max(a[1], b[1])]
                return True
            return False

        left, right = 0, 1

        while True:
            if is_interval(intervals[left],intervals[right]):
                leftv,rightv = intervals[left], intervals[right]
                intervals.remove(leftv)
                intervals.remove(rightv)
                intervals.insert(left, [min(leftv[0],rightv[0]), max(leftv[1], rightv[1])])

                left, right = 0, 1

            else:
                right += 1
                if right == len(intervals):
                    left += 1
                    right = left + 1

            if left == len(intervals) - 1:
                break
        
        return intervals