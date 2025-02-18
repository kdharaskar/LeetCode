class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+', '-', '*', '/']
        stack = []
        for token in tokens:
            if token in operations:
                if token == '+':
                    stack.append(stack.pop() + stack.pop())
                elif token == '-':
                    int1 = stack.pop()
                    int2 = stack.pop()
                    stack.append(int2 - int1)
                elif token == '*':
                    stack.append(stack.pop() * stack.pop())
                else:
                    int1 = stack.pop()
                    int2 = stack.pop()
                    stack.append(int(int2 / int1))
            else:
                stack.append(int(token))
        return stack.pop()