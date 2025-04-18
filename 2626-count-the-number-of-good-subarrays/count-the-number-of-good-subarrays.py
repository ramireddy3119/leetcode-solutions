class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        mpp = {}
        left = 0
        res = 0
        currentPairs = 0
        
        for right in range(len(nums)):
            mpp[nums[right]] = mpp.get(nums[right], 0) + 1
            currentPairs += (mpp[nums[right]] - 1)
            
            while currentPairs >= k:
                res += (len(nums) - right) 
                mpp[nums[left]] -= 1
                currentPairs -= mpp[nums[left]]
                left += 1
        
        return res
