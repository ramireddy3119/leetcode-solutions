class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            maxi = nums[i]
            mini = nums[i]
            for j in range(i,len(nums)):
                maxi = max(maxi,nums[j])
                mini = min(mini,nums[j])
                sum += maxi -mini
    
        return sum

        