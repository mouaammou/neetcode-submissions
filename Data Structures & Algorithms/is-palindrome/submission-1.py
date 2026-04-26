class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = []
        for item in s:
            if item != " " and item.isalpha() or item.isdigit():
                new_str.append(item.lower())
       
        left = 0
        right = len(new_str) - 1

        while left <= right:
            if new_str[left] != new_str[right]:
                return False
            left += 1
            right -=1

        return True
        