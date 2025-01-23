class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for number in nums:
            if number in hash:
                return True
            else:
                hash[number] = 1
        return False