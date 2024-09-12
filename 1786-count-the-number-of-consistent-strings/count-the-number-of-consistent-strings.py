class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = len(words)
        for i in words:
            for j in range(len(i)):
                if i[j] not in allowed:
                    count -= 1
                    break
        return count
        
        