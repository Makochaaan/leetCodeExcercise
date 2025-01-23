class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        length = 1
        max_length = 1
        if nums == []:
            return 0
        for n in range(len(nums)-1):
            if nums[n+1]-nums[n]==1:
                length+=1
            else:
                if max_length < length:
                    max_length = length
                length = 1
        if max_length < length:
            max_length = length
        return max_length