class Solution:
    def minLength(self, s: str) -> int:
        while True:
            f = True
            if 'AB' in s:
                s = s.replace('AB', '')
                f = False
            
            if 'CD' in s:
                s = s.replace('CD', '')
                f = False

            if f:
                return len(s)
            