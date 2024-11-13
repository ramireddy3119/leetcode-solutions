class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        for i in range(n-1):
            lb = bisect_left(nums,lower-nums[i],i+1)
            up = bisect_right(nums,upper-nums[i],i+1)
            count += (up-lb)
        return count