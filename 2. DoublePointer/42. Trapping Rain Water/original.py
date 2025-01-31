from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for n in range(max(height)):
            i = 0
            while i < len(height):
                flag = 0
                if height[i] <= n and 0<i<len(height)-1:
                    left = i-1
                    right = i+1
                    while left>=0 and right < len(height):
                        if height[left] <= n:
                            left -=1
                        elif height[right] <= n:
                            right += 1
                        else:
                            flag = 1
                            diff = right-left-1
                            res += diff
                            
                            break
                if flag == 0:
                    i += 1
                else:
                    i += diff
        return res
                    