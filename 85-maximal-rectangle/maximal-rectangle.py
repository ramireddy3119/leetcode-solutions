from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        psum = [[0] * cols for _ in range(rows)]
        
        for j in range(cols):
            sum_col = 0
            for i in range(rows):
                if matrix[i][j] == '1':
                    sum_col += 1
                else:
                    sum_col = 0
                psum[i][j] = sum_col
        
        def largestRectangleArea(heights: List[int]) -> int:
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
            max_area = 0
            for i in range(len(heights)):
                max_area = max(max_area, heights[i] * (nse[i] - pse[i] - 1))
            return max_area
        
        max_area = 0
        for i in range(rows):
            max_area = max(max_area, largestRectangleArea(psum[i]))
        
        return max_area
