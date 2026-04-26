class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for item in nums:
            if item not in seen:
                seen.add(item)
            else:
                return True
        return False