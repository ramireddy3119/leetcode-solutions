class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        l = max(nums)
        arr = [0]*(l+1)
        for i in nums:
            arr[i] += i
        print(arr)
        maxi = 0
        a = 0
        b = 0
        for i in range(l+1):
            maxi = max(a,b+arr[i])
            b = a
            a = maxi
        return maxi
        