class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMostK(nums,goal):
            if goal < 0:
                return 0
            start = 0
            sum = 0
            cnt = 0
            for end in range(len(nums)):
                sum += nums[end]

                while sum > goal:
                    sum -= nums[start]
                    start += 1
                cnt += (end - start)+1
            return cnt
        return atMostK(nums,goal)-atMostK(nums,goal-1)
