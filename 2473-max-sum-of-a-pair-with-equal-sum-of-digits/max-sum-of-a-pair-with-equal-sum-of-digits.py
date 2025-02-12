class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def isSum(n):
            summ = 0
            while n > 0:
                summ += (n%10)
                n //= 10
            return summ
        mpp = {}
        maxi = -1
        for i in range(len(nums)):
            summ = isSum(nums[i])
            if summ in mpp:
                maxi = max(maxi,mpp[summ]+nums[i])
                mpp[summ] = max(mpp[summ],nums[i])
            else:
                mpp[summ] = nums[i]
        return maxi

        