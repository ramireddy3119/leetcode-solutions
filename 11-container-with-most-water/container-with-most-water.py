class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxSum = 0
        left = 0
        right = len(height)-1

        while left < right:
            width = right - left
            heigth = min(height[left],height[right])
            current_area = width * heigth

            if current_area > maxSum:
                maxSum = current_area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxSum 



             
        