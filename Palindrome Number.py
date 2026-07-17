class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x % 10 == 0:
            return False

        s = str(x)
        l = len(s)
        count = 0

        while(True):
            if 2*count > l:
                return True
            elif s[count] != s[l-count-1]:
                return False
            
            count += 1




        