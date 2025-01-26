# longest consecutive sequence

## my answer
~~~
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub('[^a-zA-Z0-9]','',s.lower())
        for n in range(len(string)//2):
            if string[n] != string[len(string)-n-1]:
                return False
        return True
~~~

### result
status: accepted <br>
time: 5ms(87.40%) <br>
memory: 19.5mb(19.60%) <br>
comprexity: $`O(N)`$ <br>

## best solution1(using "".join, $` O(N) `$)
~~~
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        left = 0 
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
~~~

## best solution2(using [::-1], $` O(N) `$)
~~~
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]      
~~~

## point
1\. When you write [a:b:c], "a" means begin index, "b" means end index, and "c" means step. Then, [::-1] means step=-1 and begin and end isn't changed.<br>
2\. isalnum() extracts alphabet and number.<br>
3\. In join(), you can use comprehension(内包表記). <br> 
4\. When you use \W or \w as a regular expression, they excepts/contains alphabets, numbers, and under score.<br>
5\. Regular Expression is called RegEx(レジエックス，レジェックス)

## good reference
1\. Well done solution! It's almost perfect! <br>
2\. I search the string from beginning and end. <br>