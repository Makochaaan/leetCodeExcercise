<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.min.js">
</script>
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
    tex2jax: {
    inlineMath: [['$', '$'] ],
    displayMath: [ ['$$','$$'], ["\\[","\\]"] ]
    }
    });
</script>

# contains duplicate

## my answer
~~~
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for number in nums:
            if number in hash:
                return True
            else:
                hash[number] = 1
        return False        
~~~

### result
status: accepted <br>
time: 11ms (53.69%) <br>
memory: 34.82mb (9.89%) <br>

## best solution1(check length)
~~~
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)
~~~

## best solution2(sorting)
~~~
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        
        return False
~~~

## best solution3(use set)
~~~
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)
        
        return False
~~~


## point
1\. dictionary is faster than list(I experienced). <br>
2\. and set, is faster than dictionary.<br>
3\. sort method using sort algorithm, so time complexity is $ O(nlogn) $. <br>
4\. other method's complexity is $ O(n) $ . <br>

## good reference
1\. I could use hash table algorithm.(rf.Q13) <br>
2\. I solve within 2:30. <br>
