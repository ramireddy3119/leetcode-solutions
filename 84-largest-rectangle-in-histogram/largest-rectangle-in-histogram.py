class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

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
        nse = next_smaller_elements(heights)
        pse = prev_smaller_elements(heights)
        maxi = 0
        for i in range(len(heights)):
            maxi = max(maxi,heights[i]*(nse[i]-pse[i]-1))
        return maxi