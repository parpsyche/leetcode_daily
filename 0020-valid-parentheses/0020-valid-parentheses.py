class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {
            ')': '(',
            '}': '{',
            ']': '[' 
        }
        for char in s:
            if stack and char in close:
                if stack[-1] == close[char]:
                    stack.pop()
                else: return False
            else: stack.append(char)
        
        return len(stack) == 0