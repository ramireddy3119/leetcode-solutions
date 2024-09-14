class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, size = 0, 0
        tar = max(nums)
        for i in nums:
            if i == tar:
                size += 1
            else:
                size = 0
            res = max(res,size)
        return res

        