class Solution:
    def findLargestArray(self, res, used, pos, n):
        if pos == 2 * n - 1:
            return True
        if res[pos] != 0:  # Already filled
            return self.findLargestArray(res, used, pos + 1, n)

        # Try assigning all unused values
        for i in range(n, 0, -1):  # Try forming the largest number
            if used[i]:
                continue

            used[i] = True
            res[pos] = i
            if i == 1 and self.findLargestArray(res, used, pos + 1, n):
                return True
            if i > 1 and (pos + i) < (2 * n - 1) and res[pos + i] == 0:
                res[pos + i] = i
                if self.findLargestArray(res, used, pos + 1, n):
                    return True
                res[pos + i] = 0
            used[i] = False
            res[pos] = 0
        return False

    def constructDistancedSequence(self, n):
        res = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        self.findLargestArray(res, used, 0, n)
        return res