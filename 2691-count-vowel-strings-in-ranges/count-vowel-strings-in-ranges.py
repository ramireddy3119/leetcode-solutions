from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def is_vowel_word(word):
            return word[0].lower() in "aeiou" and word[-1].lower() in "aeiou"
        
        n = len(words)
        prefix_sum = [0] * (n + 1)
        
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + (1 if is_vowel_word(words[i]) else 0)
        
        res = []
        for l, r in queries:
            res.append(prefix_sum[r + 1] - prefix_sum[l])
        
        return res
