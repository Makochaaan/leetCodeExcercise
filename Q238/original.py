class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_index = -1
        for n in range(len(nums)):
            if nums[n] == 0:
                if zero_index != -1:
                    return [0 for n in range(len(nums))]
                else:
                    zero_index = n
            else:
                product = product * nums[n]
        if zero_index == -1:
            return [int(product/n) for n in nums]
        else:
            temp = [0 for n in nums]
            temp[zero_index] = product
            return temp