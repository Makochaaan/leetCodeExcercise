class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            begin = i+1
            end = len(nums)-1
            while end > begin:
                sum = nums[i]+nums[begin]+nums[end]
                if sum == 0:
                    if [nums[i],nums[begin],nums[end]] not in result:
                        result.append([nums[i],nums[begin],nums[end]])
                    begin += 1
                elif sum > 0:
                    end -= 1
                elif sum < 0:
                    begin += 1
            
        return result