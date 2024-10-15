class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0  
        zero_count = 0  

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                zero_count += 1 
            elif s[i] == '1':
                count += zero_count  
        return count

