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
            
        