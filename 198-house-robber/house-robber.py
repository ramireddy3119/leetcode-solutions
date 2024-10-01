class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def maxRob(idx):
            if idx == 0:
                return nums[idx]
            if idx < 0:
                return 0
            if idx in memo:
                return memo[idx]
            pick = nums[idx] + maxRob(idx-2)
            notpick = 0 + maxRob(idx-1)
            memo[idx] = max(pick,notpick)
            return memo[idx]
        return maxRob(len(nums)-1)
        