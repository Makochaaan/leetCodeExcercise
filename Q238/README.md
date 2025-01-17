# product of array except self

## my answer
~~~
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_index = -1
        for n in range(len(nums)):
            if nums[n] == 0:
                if zero_index != -1:
                    return [0 for n in range(len(nums))]
                else:
                    zero_index = n
            else:
                product = product * nums[n]
        if zero_index == -1:
            return [int(product/n) for n in nums]
        else:
            temp = [0 for n in nums]
            temp[zero_index] = product
            return temp   
~~~

### result
status: accepted <br>
time: 23ms (65.47%) <br>
memory: 23.15mb (69.49%) <br>

## best solution(prefix and postfix, $`O(n)`$)
~~~
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]
    
        return output        
~~~

## point
1\. define prefix as the values before the self and postfix as the values after the self. <br>
2\. firstly push the pre/post fix number and then multiple pre/post fix because the next number contains the values before self(ex. input is [2,3,4,5], and first fill with 1 and then cross 2. then next index is filled with 2). <br>
3\. the idea is suitable for all problems considering exception.

## good reference
1\. the my answer is quite original and the result rate is not bad. great job. <br>
1\. the my answer is to firstly carculate full product. <br>
