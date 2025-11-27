class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        maxi = float('-inf')

        min_prefix = {0: 0}  

        for i in range(len(nums)):
            prefix += nums[i]
            mod = (i + 1) % k

            if mod in min_prefix:
                maxi = max(maxi, prefix - min_prefix[mod])
                min_prefix[mod] = min(min_prefix[mod], prefix)
            else:
                min_prefix[mod] = prefix

        return maxi
