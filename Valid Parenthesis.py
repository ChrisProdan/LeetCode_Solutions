class Solution:
    def isValid(self, s: str) -> bool:
        Brackets = []

        for char in s:
            if char == "(":
                Brackets.append(char)
            elif char == ")":
                if len(Brackets) == 0 or Brackets[len(Brackets)-1] != "(":
                    return False
                Brackets.pop()
            elif char == "[":
                Brackets.append(char)
            elif char == "]":
                if len(Brackets) == 0 or Brackets[len(Brackets)-1] != "[":
                    return False
                Brackets.pop()
            elif char == "{":
                Brackets.append(char)
            elif char == "}":
                if len(Brackets) == 0 or Brackets[len(Brackets)-1] != "{":
                    return False
                Brackets.pop()
            
        if len(Brackets) == 0:
            return True
        else:
            return False
            
        