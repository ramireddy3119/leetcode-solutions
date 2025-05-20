class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n+1)
        for l, r in queries:
            diff[l] += 1
            diff[r+1] -= 1
        res = []
        count = 0
        for i in diff:
            count += i
            res.append(count)
        for operations, tar in zip(res,nums):
            if operations < tar:
                return False
        return True
        
