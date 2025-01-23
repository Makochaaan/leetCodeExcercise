class Solution:
    def twoSum(self, nums:list[int], target:int):
        check = {}
        for i,n in enumerate(nums):
            if target - n in check:
                return [check[target - n],i]
            else:
                check[n] = i