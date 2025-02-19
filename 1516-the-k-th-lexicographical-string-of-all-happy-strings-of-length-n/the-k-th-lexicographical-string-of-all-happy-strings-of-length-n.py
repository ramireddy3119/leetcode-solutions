class Solution:
    def getHappyString(self,n: int, k: int) -> str:
        result = []
        
        def backtrack(curr_string):
            if len(curr_string) == n:
                result.append(curr_string)
                return
            for char in "abc":
                if not curr_string or curr_string[-1] != char:
                    backtrack(curr_string + char)
        
        backtrack("")
        
        return result[k - 1] if k <= len(result) else ""

        