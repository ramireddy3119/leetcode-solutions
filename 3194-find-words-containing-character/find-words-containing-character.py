class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        arr = []
        for i,word in enumerate(words):
            if x in word:
                arr.append(i)
        return arr
        