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