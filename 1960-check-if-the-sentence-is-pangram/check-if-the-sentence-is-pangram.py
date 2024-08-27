class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ch = 97
        for _ in range(26):
            if chr(ch) not in sentence:
                return False
            ch += 1
        return True
        