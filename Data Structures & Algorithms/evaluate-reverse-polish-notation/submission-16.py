class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = set("+-/*")
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            elif len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    stack.append((a + b))
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))
        return stack[-1]