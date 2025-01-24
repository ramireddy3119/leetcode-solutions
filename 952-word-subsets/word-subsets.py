class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        freq_words2 = [0] * 26
        for word in words2:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            freq_words2 = [max(freq_words2[i], freq[i]) for i in range(26)]

        universal_words = []
        for word in words1:
            freq_word = [0] * 26
            for c in word:
                freq_word[ord(c) - ord('a')] += 1
            if all(freq_word[i] >= freq_words2[i] for i in range(26)):
                universal_words.append(word)
        return universal_words