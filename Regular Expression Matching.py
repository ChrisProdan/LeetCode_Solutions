from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache(maxsize=None)
        def recursive(s: str, p: str) -> bool:
            if len(p) >= 2 and p[1] == "*":
                return recursive(s,p[0] + p) or recursive(s,p[2:])
            elif len(s) == 0:
                return (len(p) == 0) or (len(p) == 2 and p[1] == "*")
            elif len(p) == 0:
                return (len(s) == 0)
            elif len(p) == 1:
                return (p == "." or p == s) and len(s) == 1

            elif p[0] == ".":
                return recursive(s[1:],p[1:])
            else:
                if p[0] != s[0]:
                    return False
                else:
                    return recursive(s[1:],p[1:])
        
        return recursive(s,p)