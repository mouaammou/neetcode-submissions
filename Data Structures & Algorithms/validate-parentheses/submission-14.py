class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        map_brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in set("({[") or not stack:
                stack.append(c)
            else:
                if stack and stack[-1] == map_brackets[c]:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False