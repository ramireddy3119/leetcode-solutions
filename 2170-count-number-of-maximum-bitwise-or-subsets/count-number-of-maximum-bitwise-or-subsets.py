class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxXor = 0
        for num in nums:
            maxXor |= num
        self.count = 0
        def backtrack(idx,curr):
            if len(nums) == idx:
                if curr == maxXor:
                    self.count += 1
                return
            backtrack(idx+1,curr | nums[idx])
            backtrack(idx+1,curr)
        backtrack(0,0)
        return self.count
        