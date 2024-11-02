class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        data = list(sentence.split())
        for i in range(len(data)):
            if data[i][-1] !=  data[(i+1)%len(data)][0]:
                return False
        return True 
        