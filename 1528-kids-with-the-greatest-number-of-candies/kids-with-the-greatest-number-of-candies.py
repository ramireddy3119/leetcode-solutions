class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        res = [False]*len(candies)
        for i in range(len(candies)):
            sum = extraCandies + candies[i]
            if sum >= maxi:
                res[i] = True
        return res
        