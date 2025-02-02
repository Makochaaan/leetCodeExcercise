# Valid Parentheses

## my answer
~~~
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for string in s:
            if (stack != []) and ((string == ')' and stack[-1] == '(') or (string == '}' and stack[-1] == '{') or (string == ']' and stack[-1] == '[')): 
               stack.pop()
            else:
                stack.append(string)
        if len(stack) == 0:
            return True
        else:
            return False
~~~

### result
status: accepted <br>
time: 1ms(33.00%) <br>
memory: 17.70mb(73.89%) <br>
comprexity: $`O(N)`$ <br>

## best solution1(using stack more wisely, $` O(N) `$)
~~~
class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for i in range(len(s)):
            if st:
                last = st[-1]
                if self.is_pair(last, s[i]):
                    st.pop()
                    continue
            st.append(s[i])
        
        return not st
    
    def is_pair(self, last, cur):
        if last == "(" and cur == ")" or last == "{" and cur == "}" or last == "[" and cur == "]":
            return True
        return False
~~~

## best solution2(using stack with hashmap, $` O(N) `$)
~~~
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        
        return not stack
~~~

## point
1\. Collecting the pair brutelly is one solutionally method.<br>

## good reference
1\. I've already gotten the fundamental of stack. Good.<br>