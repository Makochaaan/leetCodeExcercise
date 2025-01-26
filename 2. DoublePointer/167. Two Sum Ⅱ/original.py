class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(numbers)):
            hash[numbers[i]] = i+1
        for i in range(len(numbers)):
            m = target - numbers[i]
            if m in hash and hash[m] != i:
                return sorted([i+1,hash[m]])
        return []