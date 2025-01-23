# longest common prefix

## my answer
~~~
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        if len(strs) == 1:
            return strs[0]
        else:
            for string in strs[1:]:
                is_find = 0
                for n in range(len(prefix)+1):
                    if string.find(prefix[:n]) == 0:
                        new_prefix = prefix[:n]
                        if is_find == 0: is_find = 1
                if is_find == 0:
                    return ""
                else:
                    prefix = new_prefix
            return prefix

        
~~~

### result
status: accepted <br>
time: 2ms (84.75%) <br>
memory: 18.4mb (9.57%) <br>

## best solution
~~~
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = float("inf")
        i = 0
        for s in strs:
            if len(s) < minLength:
                minLength = len(s)
            
        while i < minLength:
            for s in strs:
                if s[i]!= strs[0][i]:
                    return s[:i]
            
            i += 1
            
        return s[:i]
~~~

### result
status: accepted <br>
time: 0ms <br>
memory : 17.4mb <br>


## point
1\. don't ignore fundamental idea(ex. In this case, you sub only if the roman number is smaller than next one. "smaller" is core idea). <br>
2\. str.replacd() returns replaced one. Cannot replace when you simply describe this function.<br>
3\. don't hesitate using "while". "for" isnn't almighty.
4\. to be strict, my 2nd answer couldn't express this case fully. Some pattern like IM is ignored.

## good reference
1\. I could put these roman numbers on dict. That's why I had to scan these strings, not numbers(rf.Q1) <br>
