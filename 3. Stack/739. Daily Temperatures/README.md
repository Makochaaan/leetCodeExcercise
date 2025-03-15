# Daily Temperatures

## my answer
~~~
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = []
        for i in range(len(temperatures)):
            stack = []
            flag = 0
            stack.append(temperatures[i])
            for j in range(i,len(temperatures)):
                    if temperatures[j] <= stack[0]:
                        stack.append(temperatures[j])
                    else:
                        res.append(len(stack)-1)
                        flag = 1
                        break
            if flag == 0:
                res.append(0)

        return res
~~~

### result
status: time out <br>
time: -- <br>
memory: -- <br>
comprexity: $`O(N^2)`$ <br>

## best solution1(using stack correctly, $` O(N) `$)
~~~
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                    index = stack.pop()
                    res[index] = i - index

            stack.append(i)

        return res
~~~

## point
1\. Integrify comparement. There's no rule that I have to judge once upon a time.<br>
2\. Initialize with zero and I don't have to put zero after judging.<br>
3\. In that case, the order(=index) is needed. Then, I have to add the order to the stack.
