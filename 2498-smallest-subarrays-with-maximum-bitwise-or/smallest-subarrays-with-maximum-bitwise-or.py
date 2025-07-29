class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [1]
        lastSeen = [-1]*32
        res = [0]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            for bit in range(32):
                if nums[i] & (1 << bit):
                    lastSeen[bit] = i
                
            max_index = i
            for bit in range(32):
                if lastSeen[bit] != -1:
                    max_index = max(max_index,lastSeen[bit])
            res[i] = max_index - i + 1
        return res

        