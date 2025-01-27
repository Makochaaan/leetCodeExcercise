# 3Sum

## my answer
~~~
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
~~~

### result
status: time out <br>
time: -- <br>
memory: -- <br>
comprexity: $`O(N)`$ <br>

## best solution1(process duplicates, $` O(N^2) `$)
~~~
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res
~~~

## best solution2(pattern matching, $` O(N^2) `$)
~~~
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()

        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return res
~~~
thanks to rowe1227.

## point
1\. set() cannot add list/dict. It could contain only elements.<br>
2\. In these solutions, the core idea to fix a number is same. However, my answer surpassed limited time. That' because I do not avoid duplicate answers.<br>
3\. To avoid duplicates, I should judge if it's same to the number before([i-1]). <br> 
4\. list.sort() doesn't produce new list(modify the original list) and sorted(list) produces new one. That means list.sort() is more efficient than sorted(list) in the point of memory complexity.<br>

## good reference
1\. The method which I take is the same as the best solution. <br>
2\. To fix one number and use two pointer is great idea. <br>