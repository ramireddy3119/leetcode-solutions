class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def countPairs(nums,mid,n):
            count = 0
            i = 1
            while i < n:
                if abs(nums[i]-nums[i-1]) <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p
        n = len(nums)
        nums.sort()
        low = 0
        high = nums[-1]
        ans = float('inf')
        while low <= high:
            mid = low + (high-low)//2
            if countPairs(nums,mid,n):
                ans = min(ans,mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans


        