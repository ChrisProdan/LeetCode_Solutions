class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        myHash = {}
        Negative = 0

        for char in t:
            if char in myHash:
                myHash[char] -= 1
            else:
                myHash[char] = -1
                Negative += 1
        

        lp = 0
        minSize = -1
        Valid = False

        for i in range(len(s)):
            if s[i] in myHash:
                if myHash[s[i]] == -1:
                    Negative -= 1
                myHash[s[i]] += 1
            
            if Negative == 0:
                Valid = True
                minSize = s[lp:i+1] if (minSize == -1 or 1 + i - lp < len(minSize)) else minSize

            while Valid and lp < i:
                if s[lp] in myHash:
                    if myHash[s[lp]] == 0:
                        Negative += 1
                        Valid = False
                    myHash[s[lp]] -= 1
                lp += 1
                minSize = s[lp:i+1] if Valid and (minSize == -1 or 1 + i -lp < len(minSize)) else minSize
            
        if minSize == -1:
            return ""
        else:
            return minSize


                





        