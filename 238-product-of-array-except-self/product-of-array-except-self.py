class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = 1
        result = [1]*len(nums)
        for i in range(len(nums)):
            result[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= suffix_product
            suffix_product *= nums[i]
        return result
        