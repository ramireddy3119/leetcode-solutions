class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = float('-inf')
        for i in accounts:
            maxi = max(maxi,sum(i))
        return maxi
        