class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Storage = dict()
        for char in s:
            if char in Storage:
                Storage[char] += 1
            else:
                Storage[char] = 1
        
        for char in t:
            if char in Storage:
                Storage[char] -= 1
            else:
                return False
        
        for x in Storage.values():
            if x != 0:
                return False
        
        return True

        