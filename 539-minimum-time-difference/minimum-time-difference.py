class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def to_minutes(t:str)->int:
            H, M = map(int,t.split(':'))
            return H * 60 + M
        
        minutes = [to_minutes(t) for t in timePoints]
        minutes.sort()

        res =  (1440 - minutes[-1]) + minutes[0]

        for i in range(len(minutes)-1):
            res = min(res, minutes[i+1]-minutes[i])
            if res == 0:
                return 0

        return res
        