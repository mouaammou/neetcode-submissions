class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        if not tokens:
            return 0
        for item in tokens:
            if item not in set("+-*/"):
                stack.append(int(item))
            elif len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                if item == '+':
                    stack.append(a + b)
                elif item == '-':
                    stack.append(a - b)
                elif item == '*':
                    stack.append(a * b)
                else:
                    if b != 0:
                        stack.append(int (a / b))

        return stack[-1]