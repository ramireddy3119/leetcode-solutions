class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def isCheck(num):
            if len(num) %2 == 1:
                return False
            left_sum = 0
            right_sum = 0
            for i in range(len(num)//2):
                left_sum += int(num[i])
                right_sum += int(num[i+len(num)//2])
            return left_sum == right_sum
        count = 0
        for i in range(low,high+1):
            if isCheck(str(i)):
                count += 1
        return count


        