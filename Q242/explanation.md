# contains duplicate

## my answer1
~~~
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s = sorted(s)
        t = sorted(t)
        for n in range(len(s)):
            if s[n] != t[n]: return False
        else: return True      
~~~

### result
status: accepted <br>
time: 19ms (17.92%) <br>
memory: 18.60mb (5.99%) <br>

## my answer2
~~~
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hash = {}
        for a in s:
            hash[a] = hash.get(a,0)+1
        for b in t:
            hash[b] = hash.get(b,0)-1
        for value in hash.values():
            if value != 0: return False
        return True
~~~

### result
status: accepted <br>
time: 11ms (74.94%) <br>
memory: 34.82mb (49.96%) <br>

## best solution1(hash table)
~~~
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  
        if len(s) != len(t):
            return False

        counter = {}

        for char in s:
            counter[char] = counter.get(char, 0) + 1

        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1

        return True
~~~

## best solution2(brute force)
~~~
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  
        if len(s) != len(t):
            return False

        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1

        for char in t:
            if count[ord(char) - ord('a')] == 0:
                return False
            count[ord(char) - ord('a')] -= 1

        return True
~~~

## point
1\. it's better to judge which method has less compexity. <br>
2\. if you sort string, use sorted(). "list".sort() is valid only for list.<br>
3\. use relative position like solution2. <br>
4\. it's better to judge which the word is contained through the second loop. <br>

## good reference
1\. I could use hash table algorithm.(rf.Q13,Q19) <br>
2\. I could use sort algorithm. <br>
