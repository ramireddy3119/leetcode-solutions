class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = []
        curr = 0
        count = 0
        for i in range(len(nums)):
            curr += nums[i]
            prefix.append(curr)
        for i in range(len(nums)-1):
            rem = prefix[-1] - prefix[i]
            if prefix[i] >= rem:
                count += 1
        return count
