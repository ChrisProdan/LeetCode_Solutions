class Solution:
    def romanToInt(self, s: str) -> int:
        Int_Map = {"M":1000,
        "D":500,
        "C":100,
        "L":50,
        "X":10,
        "V":5,
        "I":1}

        total = 0

        for i in range(len(s)):
            if i == len(s) - 1:
                return total + Int_Map[s[i]]
            elif Int_Map[s[i]] < Int_Map[s[i+1]]:
                total -= Int_Map[s[i]]
            else:
                total += Int_Map[s[i]]

        