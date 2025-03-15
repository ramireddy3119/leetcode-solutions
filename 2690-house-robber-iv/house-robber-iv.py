class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        low = min(nums)
        high = max(nums)
        mini = 0
        while low <= high:
            mid = (low+high)//2
            i = 0
            count = 0
            while i < len(nums):
                if nums[i] <= mid:
                    i += 2
                    count += 1
                else:
                    i += 1
            if count >= k:
                mini = mid
                high = mid - 1
            else:
                low = mid + 1
        return mini
        