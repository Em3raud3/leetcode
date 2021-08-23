class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) <= 1:
                return len(intervals)

        intervals = sorted(intervals, key=lambda i:i[0])

        free_room = []

        if not free_room:
                free_room.append([intervals[0][0], intervals[0][1]])
                intervals.pop(0)

        while intervals:
                next = intervals.pop(0)
                
                for index, i in enumerate(free_room):
                        if i[-1] <= next[0]:
                                free_room[index] += next
                                break
                                
                else:
                        free_room.append([next[0], next[1]])
                        
        return len(free_room)