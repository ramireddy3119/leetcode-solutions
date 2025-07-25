class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        maxi = 0
        if len(nums) == 1:
            return nums[0]
        counter = Counter(nums)
        for key,val in counter.items():
            if key > 0:
                maxi += key
        return maxi

        