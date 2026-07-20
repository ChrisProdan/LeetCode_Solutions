class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = strs[0]
        length = len(longestPrefix)
        for s in strs[1:]:
            if length == 0:
                return ""

            while longestPrefix != s[0:length]:
                length -= 1
                longestPrefix = longestPrefix[0:length]
        
        return longestPrefix

        