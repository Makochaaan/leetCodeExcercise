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