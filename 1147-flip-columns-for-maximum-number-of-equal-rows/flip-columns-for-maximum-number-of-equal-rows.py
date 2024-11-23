class Solution:
    def maxEqualRowsAfterFlips(self, matrix):
        relative_freq = Counter()

        for row in matrix:
            first = row[0]
            curr = ''.join('0' if ele == first else '1' for ele in row)
            relative_freq[curr] += 1

        return max(relative_freq.values())
