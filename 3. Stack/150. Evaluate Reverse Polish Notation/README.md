# Evaluate Reverse Polish Notation

## my answer
~~~
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+":(lambda x,y:x+y),"-":(lambda x,y:x-y),"*":(lambda x,y:x*y),"/":(lambda x,y:x/y)}
        keys = ["+","-","*","/"]
        stack = []
        for token in tokens:
            if token in keys:
                y = stack.pop()
                x = stack.pop()
                stack.append(int(operators[token](x,y)))
            else:
                stack.append(int(token))
        return stack[0]
~~~

### result
status: accepted <br>
time: 2ms(73.32%) <br>
memory: 19.23mb(17.47%) <br>
comprexity: $` O(N) `$ <br>

## best solution(Constant propagation,$` O(N) `$)
~~~
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for c in tokens:
            if c == "+":
                st.append(st.pop() + st.pop())
            elif c == "-":
                second, first = st.pop(), st.pop()
                st.append(first - second)
            elif c == "*":
                st.append(st.pop() * st.pop())
            elif c == "/":
                second, first = st.pop(), st.pop()
                st.append(int(first / second))                
            else:
                st.append(int(c))
        
        return st[0]
~~~

## point
1\. It's better in the point of complexity to reduce list/dictionary.<br>
2\. Pay attention to the orders: results are changed in subtraction/division.<br>

## good reference
1\. That's great idea to use lambda functions as values of dictionary. That reduces the amount of codes which you have ot write.<br>
2\. keys is also able to be expressed as stack.keys(), but you didn't use so that you could save memory complexity.