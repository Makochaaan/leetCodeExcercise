class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        if len(strs) == 1:
            return strs[0]
        else:
            for string in strs[1:]:
                is_find = 0
                for n in range(len(prefix)+1):
                    if string.find(prefix[:n]) == 0:
                        new_prefix = prefix[:n]
                        if is_find == 0: is_find = 1
                if is_find == 0:
                    return ""
                else:
                    prefix = new_prefix
            return prefix

        