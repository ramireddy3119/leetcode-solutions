class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # for i in range(n-k+1):
        #     temp = []
        #     curr_sum = 0
        #     flag = True
        #     for j in range(i,i+k):
        #         if nums[j] in temp:
        #             flag = False
        #             break
        #         curr_sum += nums[j]
        #         temp.append(nums[j])
        #     if flag:
        #         maxSum = max(maxSum,curr_sum)
        maxSum = 0
        windowSum = 0
        mapp = {}
        for i in range(n):
            windowSum += nums[i]
            if nums[i] in mapp:
                mapp[nums[i]] += 1
            else:
                mapp[nums[i]] = 1
            if i >= k:
                windowSum -= nums[i-k]
                mapp[nums[i-k]] -= 1
                if mapp[nums[i-k]] == 0:
                    del mapp[nums[i-k]]
            if i >= k-1 and len(mapp) == k:
                maxSum = max(maxSum,windowSum)
        return maxSum
