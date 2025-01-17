# top k frequent elements

## my answer
~~~
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        temp = []
        for num in nums:
            hash[num] = hash.get(num,0)+1
        hash = sorted(hash.items(),key=lambda x: x[1],reverse=True)
        for n in range(k):
            temp.append(hash[n][0])
        return temp  
~~~

### result
status: accepted <br>
time: 4ms (71.48%) <br>
memory: 21.19mb (52.56%) <br>

## best solution1(heap, $`O(nlogk)~O(n)`$)
~~~
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        
        return res
~~~

## best solution2(make connection in list, $`O(n)`$)
~~~
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        freq = [[] for _ in range(len(nums) + 1)]

        for n, f in counter.items():
            freq[f].append(n)
        
        res = []

        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
~~~

## point
1\. it's better to use heap structure in sorting information of size. <br>
2\. in python, heap means min heap. so you have to make the values negative<br>
3\. it's good idea to utilize the system exist. for example, regarding the index of list as frequency. <br>

## good reference
1\. I could count up using dictionary. That's great. <br>
