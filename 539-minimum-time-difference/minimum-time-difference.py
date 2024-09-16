class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def to_minutes(t:str)->int:
            H, M = map(int,t.split(':'))
            return H * 60 + M
        
        minutes = [to_minutes(t) for t in timePoints]
        minutes.sort()

        min_diff = float('inf')
        for i in range(len(minutes)-1):
            min_diff = min(min_diff, minutes[i+1]-minutes[i])
        
        min_diff = min(min_diff, (1440 - minutes[-1]) + minutes[0])

        return min_diff
        