class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        arr = set(nums)
        maxi = 0
        for num in nums:
            streak = 0
            curr = num

            while curr in arr:
                streak += 1
                curr *= curr
                if curr >= 10**5:
                    break 

            maxi = max(maxi,streak)
        
        return maxi if maxi > 1 else -1

