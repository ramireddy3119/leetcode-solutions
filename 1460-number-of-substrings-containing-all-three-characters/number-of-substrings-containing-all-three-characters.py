class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        lastSeen = {i:-1 for i in range(3)}
        for i in range(len(s)):
            lastSeen[ord(s[i])-ord('a')] = i
            if lastSeen[0] != -1 and lastSeen[2] != -1 and lastSeen[2] != -1:
                count = count + (1+min(lastSeen[0],lastSeen[1],lastSeen[2]))
        return count 
        