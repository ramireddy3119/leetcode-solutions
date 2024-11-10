from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        length = float('inf') 
        
        for i in range(len(nums)):
            xor,ans = 0,0
            for j in range(i, len(nums)):
                xor |= nums[j]  
                ans  += 1
                if xor >= k:
                    length = min(length,ans)
        
        return length if length != float('inf') else -1
