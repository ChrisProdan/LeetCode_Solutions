class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        atWord = False
        Count = 0;
        for char in s[::-1]:
            if atWord:
                if char == " ":
                    return Count
                else:
                    Count += 1
            else:
                if char != " ":
                    Count += 1
                    atWord = True
        
        return Count

        