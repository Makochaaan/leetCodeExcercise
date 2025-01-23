class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = float("inf")
        i = 0
        for s in strs:
            if len(s) < minLength:
                minLength = len(s)
            
        while i < minLength:
            for s in strs:
                if s[i]!= strs[0][i]:
                    return s[:i]
            
            i += 1
            
        return s[:i]