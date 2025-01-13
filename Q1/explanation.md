# twoSum

## my answer
~~~
class Solution:
    def twoSum(self, nums:list[int], target:int):
        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(i+1, len(nums)):
                num2 = nums[j]
                if num1 + num2 == target:
                    return [i, j]
~~~

### result
status: accepted <br>
time: 2151ms <br>
memory: 18.36mb <br>

## best solution1
~~~
class Solution:
    def twoSum(self, nums:list[int], target:int):
        check = {}
        for i,n in enumerate(nums):
            if target - n in check:
                return [check[target - n],i]
            else:
                check[n] = i
~~~

### result
status: accepted <br>
time: 0ms <br>
memory: 19mb <br>

## best solution2
~~~
class Solution:
    def twoSum(self, nums:list[int], target:int):
        for m in range(len(nums)):
            for n in range(m+1,len(nums)):
                if nums[m]+nums[n] == target:
                    return (m,n)
~~~

### result
status: accepted <br>
time: 1988ms <br>
memory : 16.4mb <br>


## point
1\. reduce redundantal injection(ex. num1 = nums[m]) <br>
2\. modify arguements <br>
3\. if you need number, make it easy to search number(ex. you don't make dict like check[i]=n. You do not need i and to search i you have to add code.) <br>

## Today's memorizing
1\. i,n in enumerate(list) : return index and content at the same time 