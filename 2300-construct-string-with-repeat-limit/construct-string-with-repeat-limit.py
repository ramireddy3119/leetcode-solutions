class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        
        maxheap = []
        for i in range(26):
            if freq[i] > 0:
                heapq.heappush(maxheap, (-i, freq[i]))
        
        res = []
        while maxheap:
            curr = heapq.heappop(maxheap)
            curr_char = chr(-curr[0] + ord('a'))
            count = min(curr[1], repeatLimit)
            res.extend([curr_char] * count)
            curr = (curr[0], curr[1] - count)
            
            if curr[1] > 0:
                if not maxheap:
                    break 
                
                next = heapq.heappop(maxheap)
                next_char = chr(-next[0] + ord('a'))
                res.append(next_char)
                next = (next[0], next[1] - 1)
                
                if next[1] > 0:
                    heapq.heappush(maxheap, next)
                heapq.heappush(maxheap, curr)
        
        return ''.join(res)