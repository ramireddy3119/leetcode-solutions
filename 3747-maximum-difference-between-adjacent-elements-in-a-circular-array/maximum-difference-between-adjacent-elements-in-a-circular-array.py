class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxi = abs(nums[0]-nums[-1])
        for i in range(1,len(nums)):
            maxi = max(maxi,abs(nums[i]-nums[i-1]))
        return maxi