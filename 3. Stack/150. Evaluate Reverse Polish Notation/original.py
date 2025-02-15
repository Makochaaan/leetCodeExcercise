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