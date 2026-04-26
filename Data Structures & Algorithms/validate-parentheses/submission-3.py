class Solution:
    def isValid(self, s: str) -> bool:
        close_brackets = set("})]")
        open_brackets = set("{([")

        count_open = 0
        count_closed = 0
        for item in s:
            if item in close_brackets:
                count_closed += 1
            if item in open_brackets:
                count_open += 1

        if count_closed != count_open:
            return False

        hash_map = {
            "}": '{',
            "]": '[',
            ")": '('
        }

        stack = []
        for item in s:
            if item in open_brackets:
                stack.append(item)
            elif stack and hash_map[item] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return True if len(stack) == 0 else False


        
