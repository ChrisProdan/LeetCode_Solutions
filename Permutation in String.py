class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        myHash = {}
        n = len(s1)

        if n > len(s2):
            return False
        nonZero = 0

        for char in s1:
            if char in myHash:
                myHash[char] -= 1
            else:
                myHash[char] = -1
                nonZero += 1
        
        for i in range(n):
            if s2[i] in myHash:

                if myHash[s2[i]] == 0:
                    nonZero += 1
                myHash[s2[i]] += 1
                if myHash[s2[i]] == 0:
                    nonZero -= 1
                
            else:
                myHash[s2[i]] = 1
                nonZero += 1
        
        if nonZero == 0:
            return True
        
        for i in range(n,len(s2)):

            if myHash[s2[i-n]] == 0:            
                nonZero += 1
            
            myHash[s2[i-n]] -= 1
        
            if myHash[s2[i-n]] == 0:
                nonZero -= 1
            
            if s2[i] in myHash:

                if myHash[s2[i]] == 0:
                    nonZero += 1
                
                myHash[s2[i]] += 1
            
                if myHash[s2[i]] == 0:
                    nonZero -= 1
            else:
                myHash[s2[i]] = 1
                nonZero += 1
        
            if nonZero == 0:
                return True

        return False



        
