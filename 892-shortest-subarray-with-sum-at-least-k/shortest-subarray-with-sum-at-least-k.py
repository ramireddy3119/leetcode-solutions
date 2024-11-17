class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dq = deque()  # Stores pairs (index, prefix_sum)
        sum_ = 0
        shortest = float('inf')

        for i in range(n):
            sum_ += nums[i]

            if sum_ >= k:
                shortest = min(shortest, i + 1)  

            while dq and (sum_ - dq[0][1] >= k):
                shortest = min(shortest, i - dq.popleft()[0])

            while dq and dq[-1][1] >= sum_:
                dq.pop()

            dq.append((i, sum_))

        return -1 if shortest == float('inf') else shortest