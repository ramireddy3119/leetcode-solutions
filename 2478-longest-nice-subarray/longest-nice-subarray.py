class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        long_sub = 0
        used = 0
        for right in range(len(nums)):
            while (used & nums[right]) != 0:
                used ^= nums[left]
                left += 1
            used |= nums[right]
            long_sub = max(long_sub,right-left+1)
        return long_sub
            
            
        