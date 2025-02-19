class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        bracketMap = {'0': '(', '1': ')'}
        for i in range(2 ** (n * 2)):
            binary = bin(i)[2:].zfill(n * 2)
            brackets = ""
            for j in binary:
                brackets += bracketMap[j]
            self.isValid(brackets) and res.append(brackets)
        
        return res

    def isValid(self, brackets: str) -> bool:
        stack = []
        bracketMap = {
            ')': '('
        }
        for bracket in brackets:
            if bracket in bracketMap:
                if len(stack) != 0 and bracketMap[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return len(stack) == 0