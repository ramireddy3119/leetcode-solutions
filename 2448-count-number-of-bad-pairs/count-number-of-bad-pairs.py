class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = 0
        mpp = {}
        for i in range(len(nums)):
            diff = i - nums[i]
            if diff in mpp:
                count += mpp[diff]
                mpp[diff] += 1
            else:
                mpp[diff] = 1


        return (len(nums)*(len(nums)-1))//2 - count
        