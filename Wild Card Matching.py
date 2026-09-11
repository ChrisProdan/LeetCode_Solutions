from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) > 0 and len(p) > 0 and p[-1] != "?" and p[-1] != "*" and (p[-1] != s[-1]):
            return False


        @lru_cache(maxsize=None)
        def recursive(s,p):
            if len(s) == 0:
                if len(p) == 0:
                    return True
                elif p[0] == "*":
                    return recursive("",p[1:])
                else:
                    return False
            elif len(p) == 0:
                return False
            elif p[0] == "*":
                return recursive(s[1:],p) or recursive(s,p[1:])
            elif p[0] == "?":
                return recursive(s[1:],p[1:])
            elif p[0] == s[0]:
                return recursive(s[1:],p[1:])
            else:
                return False
        
        return recursive(s,p)
        