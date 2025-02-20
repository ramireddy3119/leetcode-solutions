from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def backtrack(curr_str):
            if len(curr_str) == len(nums):
                if curr_str not in nums:
                    self.res = curr_str
                    return True
                return False
            
            for i in "10":
                if backtrack(curr_str + i):
                    return True
            return False
        
        self.res = ""
        backtrack("")
        return self.res
