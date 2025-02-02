class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        c=0
        for i in range(n):
            if(nums[i]>nums[(i+1)%n]):
                c+=1
        return c<=1