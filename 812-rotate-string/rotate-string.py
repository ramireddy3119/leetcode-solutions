class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n1 = len(s)
        n2 = len(goal)

        if n1 != n2:
            return False
        for i in range(n1):
            r = s[i:] + s[:i]
            if r == goal:
                return True
        return False
        