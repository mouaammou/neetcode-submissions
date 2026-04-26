class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operations = set("*/+-")
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in operations:
                stack.append(int(tokens[i]))
            elif len(stack) >= 2:
                opera = tokens[i]
                elment_2 = stack.pop()
                elment_1 = stack.pop()

                if opera == "+":
                    stack.append(elment_1 + elment_2)
                elif opera == "-":
                    stack.append(elment_1 - elment_2)
                elif opera == "*":
                    stack.append(elment_1 * elment_2)
                else:
                    if elment_2 != 0:
                        stack.append(int(elment_1 / elment_2) )

        return stack[-1]