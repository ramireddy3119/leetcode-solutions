class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        fst = {}
        lst = {}
        for i,ch in enumerate(s):
            if ch not in fst:
                fst[ch] = i
            lst[ch] = i
        
        unique = set()
        for ch in fst:
            if fst[ch] < lst[ch]:
                mdl = s[fst[ch] + 1: lst[ch]]
                for c in set(mdl):
                    unique.add((ch,c,ch))
        return len(unique)