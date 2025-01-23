# longest consecutive sequence

## my answer
~~~
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        length = 1
        max_length = 1
        if nums == []:
            return 0
        for n in range(len(nums)-1):
            if nums[n+1]-nums[n]==1:
                length+=1
            else:
                if max_length < length:
                    max_length = length
                length = 1
        if max_length < length:
            max_length = length
        return max_length
~~~

### result
status: accepted <br>
time: 35ms(97.71%) <br>
memory: 34mb(39.16%) <br>
comprexity: $`O(NlogN)`$ <br>

## best solution1(semi-brute force, $` O(N) `$)
~~~
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in num_set:
                length = 1

                while n + length in num_set:
                    length += 1
                
                longest = max(longest, length)
        
        return longest
~~~

## point
1\. set() is primarily adopt the original sequence(ex. set(sorted(list)) returns a list which sequence is same as original list.) <br>
2\. check consequence, then check below/above contents.<br>

## good reference
1\. Well done solution! I could check the below/above numbers to decide the consecutiveness. <br>
2\. in O(NlogN), comprexity increases more smoothly than in O(N). <br>