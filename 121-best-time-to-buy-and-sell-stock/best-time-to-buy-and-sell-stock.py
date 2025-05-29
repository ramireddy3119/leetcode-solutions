class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        mini=prices[0]
        maxi=0
        for i in range(1,n):
            if prices[i]<mini:
                mini=prices[i]
            else:
                maxi=max(prices[i]-mini,maxi)
        return maxi

       


        