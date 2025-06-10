class Solution:
    def maxDifference(self, s: str) -> int:
        map = {}
        for i in s:
            map[i] = map.get(i,0)+1
        even = float('inf')
        odd = 0
        for val in map.values():
            if val % 2 == 0:
                even = min(even,val)
            else:
                odd = max(odd,val)
        return odd-even        