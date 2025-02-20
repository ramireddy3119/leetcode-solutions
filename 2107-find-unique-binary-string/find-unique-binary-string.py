class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def backtrack(curr_str):
            if len(curr_str) == len(nums):
                if curr_str not in nums:
                    res.append(curr_str)
                    return
            for i in "10":
                if curr_str not in nums:
                    backtrack(curr_str+i)
        res = []
        backtrack("")
        return res[0]

        