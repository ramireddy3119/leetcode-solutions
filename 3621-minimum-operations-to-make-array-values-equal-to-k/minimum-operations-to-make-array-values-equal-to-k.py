class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sett = set()
        for i in nums:
            if i < k:
                return -1
            elif i > k:
                sett.add(i)
        return len(sett)
        