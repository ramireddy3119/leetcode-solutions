from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        for i in range(n):
            left = i + 1
            right = n - 1
            # find minimum j where nums[i] + nums[j] >= lower
            while left <= right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] >= lower:
                    right = mid - 1
                else:
                    left = mid + 1
            l = left
            
            left = i + 1
            right = n - 1
            # find maximum j where nums[i] + nums[j] <= upper
            while left <= right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] <= upper:
                    left = mid + 1
                else:
                    right = mid - 1
            r = right
            
            if l <= r:
                count += (r - l + 1)
                
        return count
