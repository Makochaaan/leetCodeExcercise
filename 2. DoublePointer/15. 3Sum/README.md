# 3Sum

## my answer
~~~
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            begin = i+1
            end = len(nums)-1
            while end > begin:
                sum = nums[i]+nums[begin]+nums[end]
                if sum == 0:
                    if [nums[i],nums[begin],nums[end]] not in result:
                        result.append([nums[i],nums[begin],nums[end]])
                    begin += 1
                elif sum > 0:
                    end -= 1
                elif sum < 0:
                    begin += 1
            
        return result
~~~

### result
status: time out <br>
time: -- <br>
memory: -- <br>
comprexity: $`O(N)`$ <br>

## best solution(using "".join, $` O(N^2) `$)
~~~
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res
~~~

## point
1\. set() cannot add list/dict. It could contain only elements.<br>
2\. In these solutions, the core idea to fix a number is same. However, my answer surpassed limited time. That' because I do not avoid duplicate answers.<br>
3\. To avoid duplicates, I should judge if it's same to the number before([i-1]). <br> 
4\. list.sort() doesn't produce new list(modify the original list) and sorted(list) produces new one. That means list.sort() is more efficient than sorted(list) in the point of memory complexity.<br>

## good reference
1\. The method which I take is the same as the best solution. <br>
2\. To fix one number and use two pointer is great idea. <br>