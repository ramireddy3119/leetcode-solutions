class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(freq):
            ways = 0
            for i in range(26):
                if freq[i] > 0:
                    freq[i] -= 1
                    ways += 1 + backtrack(freq)
                    freq[i] += 1
            return ways
        freq = [0]*26
        for c in tiles:
            freq[ord(c) - ord('A')] += 1
        return backtrack(freq)
            
        