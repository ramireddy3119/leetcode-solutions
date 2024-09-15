class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = 'aeiou'
        res = 0
        mask = 0
        mask_to_indx = {0:-1}
        
        for i, c in enumerate(s):
            if c in vowels:
                mask = mask ^ (1 + ord(c)-ord('a'))
            
            if mask in mask_to_indx:
                length = i - mask_to_indx[mask]
                res = max(res,length)
            else:
                mask_to_indx[mask] = i
        return res

        