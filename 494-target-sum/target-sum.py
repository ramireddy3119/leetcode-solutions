from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def countPartitionsUtil(ind,tar,arr,dp):
            if ind  == 0:
                if tar == 0 and arr[0] == 0: return 2
                if tar == 0 or tar == arr[0]: return 1
                return 0
            if dp[ind][tar] != -1:
                return dp[ind][tar]
            
            notTake = countPartitionsUtil(ind-1,tar,arr,dp)
            take = 0
            if arr[ind] <= tar:
                take = countPartitionsUtil(ind-1,tar-arr[ind],arr,dp)
            dp[ind][tar] = (take+notTake)
            return dp[ind][tar]
        def findWays(arr,d):
            n = len(arr)
            totSum = sum(arr)
            
            if totSum - d < 0: return 0
            if (totSum - d) % 2 == 1: return 0
            
            s2 = (totSum-d)//2
            dp  = [[-1 for j in range(s2+1)]for i in range(n)]
            return countPartitionsUtil(n-1,s2,arr,dp)
        return findWays(nums,target)
