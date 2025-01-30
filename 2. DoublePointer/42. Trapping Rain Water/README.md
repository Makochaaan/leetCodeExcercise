# Trapping Rain Water

## my answer
~~~
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
~~~

### result
status: time out <br>
time: -- <br>
memory: -- <br>
comprexity: $` O(N^2) `$ <br>

## best solution1(process duplicates, $` O(N^2) `$)
~~~
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        
        return water
~~~

## point
1\. If the height drops, trapping area is expanded.<br>
2\. Memorize maximum numbers, and you can judge the height drops or not.<br>

## good reference
1\. Not bad idea to search by one height. <br>