class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            mini = min(nums)
            nums[nums.index(mini)] = mini * multiplier
        return nums 
        