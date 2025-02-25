class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [] 
        max_area = 0
    
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                width = i if not stack else (i - stack[-1] - 1)
                max_area = max(max_area, height * width)
            stack.append(i)

        while stack:
            height = heights[stack.pop()]
            width = n if not stack else (n - stack[-1] - 1)
            max_area = max(max_area, height * width)
    
        return max_area
        