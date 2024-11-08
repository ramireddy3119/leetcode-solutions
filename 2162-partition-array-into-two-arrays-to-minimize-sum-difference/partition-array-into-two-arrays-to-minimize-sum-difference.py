from typing import List
from bisect import bisect_left

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        N = n // 2
        left, right = [[] for _ in range(N + 1)], [[] for _ in range(N + 1)]

        for mask in range(1 << N):
            l_sum = r_sum = idx = 0
            for i in range(N):
                if mask & (1 << i):
                    idx += 1
                    l_sum += nums[i]
                    r_sum += nums[i + N]
            left[idx].append(l_sum)
            right[idx].append(r_sum)

        for idx in range(N + 1):
            right[idx].sort()

        result = min(abs(total_sum - 2 * left[N][0]), abs(total_sum - 2 * right[N][0]))

        for idx in range(1, N):
            for a in left[idx]:
                target = (total_sum - 2 * a) // 2
                right_idx = N - idx
                v = right[right_idx]

                pos = bisect_left(v, target)

                if pos < len(v):
                    result = min(result, abs(total_sum - 2 * (a + v[pos])))
                if pos > 0:
                    result = min(result, abs(total_sum - 2 * (a + v[pos - 1])))

        return result
