class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        my_checker = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for item in s:
            open_bra = set('{[(')

            if item in open_bra:
                stack.append(item)
            elif stack and  stack[-1] == my_checker[item]:
                stack.pop()
            else: return False

        if stack: return False
        return True
