class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start,curr):
            res.append(curr)

            for i in range(start,len(nums)):
                backtrack(i+1,curr+[nums[i]])
        res = []
        backtrack(0,[])
        print(res)
        return res


        