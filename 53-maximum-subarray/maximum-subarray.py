class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        sum = 0
        for right in range(len(nums)):
            sum += nums[right]
            maxi = max(sum,maxi)
            if sum < 0:
                sum = 0
        return maxi
        