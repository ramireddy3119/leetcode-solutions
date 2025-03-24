from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days

        meetings.sort()
        free_days = meetings[0][0] - 1 
        end = meetings[0][1]

        for i in range(1, len(meetings)):
            if meetings[i][0] > end:
                free_days += meetings[i][0] - end - 1
            end = max(end, meetings[i][1])
        
        free_days += days - end 
        return free_days
