class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = list(str(num))
        for ch in s:
            if ch != '9':
                max_num = int(''.join(['9' if x == ch else x for x in s]))
                break
        else:
            max_num = num  

        for ch in s:
            if ch != '0':
                min_num = int(''.join(['0' if x == ch else x for x in s]))
                break
        else:
            min_num = num 

        return max_num - min_num
