# roman to integer

## my 1st answer
~~~
class Solution:
    
    def romanToInt(self, s: str) -> int:
        number = 0
        while True:
            if s.find("IV") == -1: break
            s.replace("IV","")
            number += 4
        while True:
            if s.find("IX") == -1: break
            s.replace("IX","")
            number += 9
        while True:
            if s.find("XL") == -1: break
            s.replace("XL","")
            number += 40
        while True:
            if s.find("XC") == -1: break
            s.replace("XC","")
            number += 90
        while True:
            if s.find("CD") == -1: break
            s.replace("CD","")
            number += 400
        while True:
            if s.find("CM") == -1: break
            s.replace("CM","")
            number += 900
        for string in s:
            if string == "I":
                number += 1
            elif string == "V":
                number += 5
            elif string == "X":
                number += 10
            elif string == "L":
                number += 50
            elif string == "C":
                number += 100
            elif string == "D":
                number += 500
            elif string == "M":
                number += 1000
        return number
~~~

### result
status: denied <br>
time: time out <br>
memory: -- <br>

## my 2nd answer
~~~
class Solution:
    
    def romanToInt(self, s: str) -> int:
        number = 0
        substraction = {
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        for key in substraction.keys():
            count = s.count(key)
            for n in range(count):
                if  s.find(key) !=-1:
                    s = s.replace(key,"",1)
                    number += substraction[key]
        for string in s:
            if string == "I":
                number += 1
            elif string == "V":
                number += 5
            elif string == "X":
                number += 10
            elif string == "L":
                number += 50
            elif string == "C":
                number += 100
            elif string == "D":
                number += 500
            elif string == "M":
                number += 1000
        return number
~~~

### result
status: accepted <br>
time: 2ms (84.75%) <br>
memory: 18.4mb (9.57%) <br>

## best solution
~~~
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L': 50, 'C': 100, 'D':500, 'M': 1000}
        num = 0
        i = 0
        while (i < len(s)):
            if (i < (len(s) - 1)):
                if (dic[s[i]] >= dic[s[i+1]]):
                    num += dic[s[i]]
                    i += 1
                elif (dic[s[i]] < dic[s[i+1]]):
                    num += (dic[s[i+1]] - dic[s[i]])
                    i += 2

            else:
                num += dic[s[i]]
                i += 1

        return num
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
