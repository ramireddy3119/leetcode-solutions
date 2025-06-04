class Solution:
    def squareIsWhite(self, s: str) -> bool:
      
       return (ord(s[0])+int(s[1]))%2 != 0
        