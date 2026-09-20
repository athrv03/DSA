class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeopen={")":"(","}":"{","]":"["}

        for char in s:
            if char in closeopen:
                if stack and stack[-1]==closeopen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False

            
        
                




        