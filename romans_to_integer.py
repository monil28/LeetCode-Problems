"""
    Problem Statement Link :- https://leetcode.com/problems/roman-to-integer/
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            'IV': 4,
            'IX': 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900
        }
        total = 0 
        j=0
        l = len(s)
        while j<=l-1:
            if j!=l-1:
                if s[j] == 'I' or s[j] == "X" or s[j] == "C":
                    num = s[j]+s[j+1]
                    if num in romans:
                        total += romans[num]
                        j+=2     
                    else:
                        total += romans[s[j]]
                        j+=1
                else:
                    total += romans[s[j]]
                    j+=1
            else:
                total += romans[s[j]]
                j+=1

        return total