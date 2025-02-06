class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        def countTuple(k):
            return k * (k-1)//2
        mpp = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product = nums[i] * nums[j]
                if product in mpp:
                    mpp[product] += 1
                else:
                    mpp[product] = 1
        count = 0
        for i in mpp.values():
            count += countTuple(i) * 8
        return count

        