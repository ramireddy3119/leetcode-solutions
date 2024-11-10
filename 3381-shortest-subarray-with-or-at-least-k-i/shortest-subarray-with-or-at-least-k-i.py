class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        if k == 0:
            return 1
        
        precomp = [0] * 32
        st = 0
        ans = float('inf')
        
        for i in range(len(nums)):
            val = 0
            for j in range(32):
                if nums[i] & (1 << j):
                    precomp[j] += 1
                if precomp[j]:
                    val |= (1 << j)
            
            if val >= k:
                ans = min(ans, i - st + 1)
            
            while val >= k:
                val = 0
                for j in range(32):
                    if nums[st] & (1 << j):
                        precomp[j] -= 1
                    if precomp[j]:
                        val |= (1 << j)
                st += 1
                
                if val >= k:
                    ans = min(ans, i - st + 1)
        
        return ans if ans != float('inf') else -1
