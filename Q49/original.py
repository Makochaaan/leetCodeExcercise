class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        for n in range(len(strs)):
            hash = {}
            temp = []
            temp.append(strs[n])
            for char in strs[n]:
                hash[char] = hash.get(char,0)+1
            for m in range(n+1,len(strs)):
                hash2 = hash
                for char in strs[m]:
                    if hash2.get(char,0)-1 >= 0:
                        hash2[char] = hash2.get(char,0)-1

                if any(hash2.values()) == False:
                    temp.append(strs[m])
            result.append(temp)

        return result


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        checked = [False] * len(strs)
        for m in range(len(strs)):
            if not checked[m]:
                temp = [strs[m]]
                checked[m] = True
                for n in range(m+1,len(strs)):
                    if sorted(strs[m]) == sorted(strs[n]): 
                        temp.append(strs[n])
                        checked[n] = True
                result.append(temp)

        return result