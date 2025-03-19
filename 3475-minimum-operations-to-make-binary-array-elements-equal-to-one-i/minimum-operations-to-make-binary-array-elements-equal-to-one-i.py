class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def flipBits(pos):
            nums[pos] ^= 1
            nums[pos+1] ^= 1
            nums[pos+2] ^= 1
        n = len(nums)
        cnt = 0
        for i in range(n-2):
            if nums[i] == 0:
                flipBits(i)
                cnt += 1
        if nums[n-1]==0 or nums[n-2]==0:
            return -1
        return cnt
        