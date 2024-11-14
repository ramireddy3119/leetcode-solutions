from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def findWays(nums,tar):
            n = len(nums)
            dp = [[0]*(tar+1) for _ in range(n)]
            if nums[0] == 0:
                dp[0][0] = 2
            else:
                dp[0][0] = 1
            if nums[0] <= tar and nums[0] != 0:
                dp[0][nums[0]] = 1
            for ind in range(1,n):
                for target in range(tar+1):
                    notTaken = dp[ind-1][target]
                    take = 0
                    if nums[ind] <= target:
                        take = dp[ind-1][target-nums[ind]]
                    dp[ind][target] = take + notTaken
            return dp[n-1][tar]
        totSum = sum(nums)
        if totSum - target < 0: return 0
        if (totSum - target) % 2 == 1: return 0
        return findWays(nums,(totSum-target)//2)