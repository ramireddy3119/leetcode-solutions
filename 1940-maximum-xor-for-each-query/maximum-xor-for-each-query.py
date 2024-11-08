from typing import List
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix_xor = []
        prefix = 0
        for i in range(len(nums)):
            prefix ^= nums[i]
            prefix_xor.append(prefix)
        res = []
        k = (1 << maximumBit) - 1
        for i in range(len(nums)-1,-1,-1):
            res.append(prefix_xor[i] ^ k) 
        

        return res
        