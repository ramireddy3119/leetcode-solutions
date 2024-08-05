class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen = 0
        l =0
        r =0
        zero = 0
        while r < len(nums):
            if nums[r] == 0:
                zero += 1
            while zero > k:
                if nums[l] == 0:
                    zero -= 1
                l += 1
            maxlen = max(maxlen,r-l+1)
            r += 1
        return maxlen
            

