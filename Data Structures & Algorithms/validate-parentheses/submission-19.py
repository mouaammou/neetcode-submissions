class Solution:
    def isValid(self, s: str) -> bool:
        # if not str:
        #     return False
        
        stack = []

        brackets = {
            ']': '[',
            '}': '{', 
            ')': '(',
        }



        for item in s:
            open_brackts = set("({[")

            if item in open_brackts:
                stack.append(item)
            else:
                if stack and stack[-1] == brackets[item]:
                    stack.pop()
                else:
                    return False
            
        return True if not stack else False