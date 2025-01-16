# group anagrams

## my answer1
~~~
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        for n in range(len(strs)):
            hash = {}
            temp = []
            temp.append(strs[n])
            for char in strs[n]:
                hash[char] = hash.get(char,0)+1
            for m in range(n+1,len(strs)):
                hash2 = hash
                for char in strs[m]:
                    if hash2.get(char,0)-1 >= 0:
                        hash2[char] = hash2.get(char,0)-1

                if any(hash2.values()) == False:
                    temp.append(strs[m])
            result.append(temp)

        return result  
~~~

### result
status: denied <br>
time: -- <br>
memory: -- <br>

## my answer2(sorting)
~~~
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        checked = [False] * len(strs)
        for m in range(len(strs)):
            if not checked[m]:
                temp = [strs[m]]
                checked[m] = True
                for n in range(m+1,len(strs)):
                    if sorted(strs[m]) == sorted(strs[n]): 
                        temp.append(strs[n])
                        checked[n] = True
                result.append(temp)

        return result
~~~

### result
status: timed out <br>
time: -- <br>
memory: -- <br>

## best solution1(sorting, O(mnlogn))
~~~
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
        
        return list(ans.values())
~~~

## best solution2(hash table using ASCII, O(mn))
~~~
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        
        return list(ans.values())
~~~

## point
1\. this problem, never use hash table because there are too many substruction of values. <br>
2\. in sorting method, checking list made the process slower.<br>
3\. defaultdict(list) is a dictionary which can be translated to list. However, it's not necessary. <br>
4\. What I need is to store list and store sorted string as a key. Referencing the sorted key, I can append what I want. <br>
5\. in ASCII method, just the key is changed to list.<br>

## good reference
1\. Nothing. <br>
