class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        j = 0
        while i < len(str1) and j < len(str2):
            diff = ord(str2[j])-ord(str1[i]) 
            if str1[i] == str2[j] or diff == 1 or diff == -25:
                j += 1
            i += 1
        if j == len(str2):
            return True
        else:
            return False
