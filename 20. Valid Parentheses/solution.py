class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c in bracketMap:
                if len(stack) == 0:
                    return False
                if stack[-1] == bracketMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0