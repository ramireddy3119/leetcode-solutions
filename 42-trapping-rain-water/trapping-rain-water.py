class Solution:
    def trap(self, height: List[int]) -> int:
        total =0
        leftMax = 0
        rightMax = 0
        l = 0
        r = len(height)-1
        while l < r:
            if height[l] <= height[r]:
                if leftMax > height[l]:
                    total += leftMax - height[l]
                else:
                    leftMax = height[l]
                l += 1
            else:
                if rightMax > height[r]:
                    total += rightMax - height[r]
                else:
                    rightMax = height[r]
                r -= 1
        return total


        