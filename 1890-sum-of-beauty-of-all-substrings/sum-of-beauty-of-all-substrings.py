class Solution:
    def beautySum(self,s: str) -> int:
        n = len(s)
        total_beauty = 0

    
        for i in range(n):
            freq = {}  
            for j in range(i, n):
                char = s[j]
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
                max_freq = max(freq.values())
                min_freq = min(freq.values())
            
                total_beauty += max_freq - min_freq
    
        return total_beauty


