# Two Sum Ⅱ

## my answer
~~~
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(numbers)):
            hash[numbers[i]] = i+1
        for i in range(len(numbers)):
            m = target - numbers[i]
            if m in hash and hash[m] != i:
                return sorted([i+1,hash[m]])
        return []
~~~

### result
status: accepted <br>
time: 5ms(37.81%) <br>
memory: 18.77mb(6.93%) <br>
comprexity: $`O(N)`$ <br>

## best solution1(make use of the array rule, $` O(N) `$)
~~~
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            else:
                left += 1
~~~

## point
1\. If the sum is above the target, you can make end pointer less, and vice versa(cf. newton method).<br>

## good reference
1\. The answer is not bit a wise, but I can advance my past knowledge. <br>