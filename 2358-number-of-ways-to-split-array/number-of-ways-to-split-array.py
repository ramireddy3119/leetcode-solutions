class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = []
        curr = 0
        count = 0
        # for i in range(len(nums)):
        #     curr += nums[i]
        #     prefix.append(curr)
        totalSum = 0
        for i in nums:
            totalSum += i
        
        for i in range(len(nums)-1):
            curr += nums[i]
            rem = totalSum - curr
            if curr >= rem:
                count += 1
        return count
