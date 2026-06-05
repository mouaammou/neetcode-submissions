class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        res = 0
        for r in range(len(s2)):
            if r - l + 1 == len(s1):
                substr = s2[l: r + 1]
                substr = sorted(substr)
                if substr == sorted(s1):
                    return True
                l += 1
        return False