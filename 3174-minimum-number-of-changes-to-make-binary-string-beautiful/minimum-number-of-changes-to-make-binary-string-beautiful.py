class Solution:
    def minChanges(self, s: str) -> int:
        start = 0
        i = 1
        count = 0
        odd = []
        while i < len(s):
            while i < len(s) and s[i] == s[i-1]:
                i += 1
            
            if (i - start) % 2 == 1:
                odd.append(count) 
            start = i
            count += 1
            i+=1
        if (i-start)%2 == 1:
            odd.append(count)
        mini = 0
        for i in range(1,len(odd),2):
            mini += odd[i] - odd[i-1]
        return mini

        