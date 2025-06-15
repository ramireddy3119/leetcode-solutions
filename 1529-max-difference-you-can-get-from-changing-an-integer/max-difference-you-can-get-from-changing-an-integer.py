class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        
        for c in s:
            if c != '9':
                max_num = int(s.replace(c, '9'))
                break
        else:
            max_num = num  
        if s[0] != '1':
            min_num = int(s.replace(s[0], '1'))
        else:
            for i in range(1, len(s)):
                if s[i] not in ('0', '1'):
                    min_num = int(s.replace(s[i], '0'))
                    break
            else:
                min_num = num
        
        return max_num - min_num
