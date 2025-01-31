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