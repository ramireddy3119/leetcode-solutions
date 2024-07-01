class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        arr = [[]]
        for i in range(1<<n):
            sub = []
            for j in range(n):
                if i&(1<<j)!=0:
                    sub.append(nums[j])
            if sub:
                arr.append(sub)
        return arr

        