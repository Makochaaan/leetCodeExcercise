class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            print(key)
            ans[key].append(s)
            print(ans)
        
        return list(ans.values())

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        
        return list(ans.values())
    