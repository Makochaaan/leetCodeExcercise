class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
    
class Solution(object):
    def maxArea(self, height):
        lp = 0
        rp = len(height) - 1
        max_h = max(height)
        max_area = (rp - lp )*min(height[lp],height[rp])
        while lp < rp:
            if height[lp] >= height[rp]: #right side shorter
                area = (rp - lp )*height[rp]
                max_area = area if area > max_area else max_area
                if max_area >= max_h * (rp - lp ):
                    break
                rp -= 1
                continue
            else: #left side shorter
                area = (rp - lp )*height[lp]
                max_area = area if area > max_area else max_area
                if max_area >= max_h * (rp - lp ):
                    break
                lp += 1
                continue
        return max_area