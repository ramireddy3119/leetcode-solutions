class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count = 1
        maxi = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                maxi = max(maxi,count)
                count = 1
        maxi = max(maxi,count)
        count = 1 
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
            else:
                maxi = max(maxi,count)
                count = 1
        maxi = max(maxi,count)
        return maxi