class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n==1: return cost[0]
        if n==2: return min(cost[0],cost[1])

        first = cost[0]
        second = cost[1]

        for i in range(2,len(cost)):
            current = min(first,second)+cost[i]
            first = second 
            second = current
        
        return min(first,second)