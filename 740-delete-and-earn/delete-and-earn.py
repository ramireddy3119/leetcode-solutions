class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        arr = [0]*10001
        for i in nums:
            arr[i] += i
        print(arr)
        maxi = 0
        a = 0
        b = 0
        for i in range(10001):
            maxi = max(a,b+arr[i])
            b = a
            a = maxi
        return maxi
        