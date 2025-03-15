# Generate Parentheses

## my answer is None

## best solution1(using state and stack, $` O(N) `$)
~~~
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        left = right = 0
        q = [(left, right, '')]
        while q:
            left, right, s = q.pop()
            if len(s) == 2 * n:
                result.append(s)
            if left < n:
                q.append((left + 1, right, s + '('))
            if right < left:
                q.append((left, right + 1, s + ')'))
        return result
~~~

## best solution2(using function, $` O(N) `$)
~~~
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def diffs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return
            
            if left < n:
                diffs(left+1,right,s+"(")
            
            if right < left:
                diffs(left,right+1,s+")")

        diffs(0,0,"")

        return res
~~~

## point
1\. Comparing to judging validation, generation is more complicated.<br>
2\. If you want to branch the result, use function recursion like solution2.<br>
3\. It's also the way to memorize variants belong to what you need.
