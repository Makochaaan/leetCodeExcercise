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