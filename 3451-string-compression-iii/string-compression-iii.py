class Solution:
    def compressedString(self, word: str) -> str:
        i = 1
        res = ""
        start = 0
        while i < len(word):
            while i < len(word) and word[i] == word[i-1] and (i-start) <=9:
                i += 1
            if (i-start) == 10: i -= 1
            res += str(i-start)
            res += word[start]
            start = i
            i += 1
        if start == len(word)-1:
            res += str(i-start)
            res += word[start]
        return res

            
            
        