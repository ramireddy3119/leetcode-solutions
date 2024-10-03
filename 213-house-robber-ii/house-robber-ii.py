class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        def solve(nums):
            n = len(nums)
            prev = nums[0]
            prev2 = 0
            
            for i in range(1,n):
                pick = nums[i]
                if i > 1:
                    pick += prev2
                notPick = prev

                curr = max(pick,notPick)
                prev2 = prev
                prev = curr
            return prev
        temp1 = []
        temp2 = []
        for i in range(n):
            if i != 0:
                temp1.append(nums[i])
            if i != n-1:
                temp2.append(nums[i])
        return max(solve(temp1),solve(temp2))
        