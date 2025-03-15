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