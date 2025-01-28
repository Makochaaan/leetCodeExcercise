class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = len(height)-1
        l = 0
        temp = 0
        while r> l:
            if temp < min(height[r],height[l])*(r-l):
                temp = min(height[r],height[l])*(r-l)
            if height[l] <= height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
        return temp