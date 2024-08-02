class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        
        def next_smaller_elements(arr):
            nse = [0] * len(arr)
            stack = []
            for i in range(len(arr) - 1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                nse[i] = len(arr) if not stack else stack[-1]
                stack.append(i)
            return nse
        
        def prev_smaller_elements(arr):
            pse = [0] * len(arr)
            stack = []
            for i in range(len(arr)):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                pse[i] = -1 if not stack else stack[-1]
                stack.append(i)
            return pse
        
        total_sum = 0
        nse = next_smaller_elements(arr)
        pse = prev_smaller_elements(arr)
        
        for i in range(len(arr)):
            left = i - pse[i]
            right = nse[i] - i
            total_sum = (total_sum + (right * left * arr[i]) % mod) % mod
        
        return total_sum
