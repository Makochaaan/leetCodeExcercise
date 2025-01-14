class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s = sorted(s)
        t = sorted(t)
        for n in range(len(s)):
            if s[n] != t[n]: return False
        else: return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hash = {}
        for a in s:
            hash[a] = hash.get(a,0)+1
        for b in t:
            hash[b] = hash.get(b,0)-1
        for value in hash.values():
            if value != 0: return False
        return True