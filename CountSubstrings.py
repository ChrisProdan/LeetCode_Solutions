class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        Width = 0
        total = 0
        for i in range(len(s)):
            while True:

                if i - Width < 0 or i + Width >= n:
                    Width = 0
                    break
                elif s[i - Width] != s[i + Width]:
                    Width = 0
                    break
                else:
                    total += 1
                    Width += 1

        Width = 0

        for i in range(len(s)):
            while True:

                if i - Width < 0 or i+1 + Width >= n:
                    Width = 0
                    break
                elif s[i - Width] != s[i + 1 + Width]:
                    Width = 0
                    break
                else:
                    total += 1
                    Width += 1
        
        return total

            


        