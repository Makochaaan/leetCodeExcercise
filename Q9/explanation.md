# twoSum

## my answer
~~~
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        if y == y[::-1]:
            return True
        else:
            return False
~~~

### result
status: accepted <br>
time: 4ms <br>
memory: 17.67mb <br>

## best solution1
~~~
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
~~~

### result
status: accepted <br>
time: 0ms <br>
memory: 1mb <br>

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
