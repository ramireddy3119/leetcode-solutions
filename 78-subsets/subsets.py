class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start,curr):
            res.append(curr[:])

            for i in range(start,len(nums)):
                curr.append(nums[i])
                backtrack(i+1,curr)
                curr.pop()

                
        res = []
        backtrack(0,[])
        return res


        