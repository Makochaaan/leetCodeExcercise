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

            
        