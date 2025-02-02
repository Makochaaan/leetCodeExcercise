# Min Stack

## my answer
~~~
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack != []:
            return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
~~~

### result
status: accepted <br>
time: 135ms(6.15%) <br>
memory: 21.23mb(78.94%) <br>

## best solution1(using two stack)
~~~
class MinStack:

    def __init__(self):
        self.stk = []
        self.mstk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.mstk) == 0: #empty
            self.mstk.append(val)
        elif val < self.mstk[-1]: #new min
            self.mstk.append(val)
        else: #keep min
            self.mstk.append(self.mstk[-1])

    def pop(self) -> None:
        self.stk.pop()
        self.mstk.pop()
        
    def top(self) -> int:
        return self.stk[-1]
        
    def getMin(self) -> int:
        return self.mstk[-1]
~~~

## best solution2(contains list in the stack)
~~~
class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val == None or min_val > val:
            min_val = val
        
        self.st.append([val, min_val])

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0] if self.st else None

    def getMin(self) -> int:
        return self.st[-1][1] if self.st else None
~~~

## point
1\. Min stack is a stack that we can store the max number at the same time to add number into the stack.<br>
2\. You can call the class method in the same class using self.<br>
3\. You can use if-else in return call.<br>

## good reference
1\. Nothing. You missed diffinition. That's just a ordinary stack.<br>