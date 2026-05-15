class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        map_brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in map_brackets:
                if stack and stack[-1] == map_brackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

        