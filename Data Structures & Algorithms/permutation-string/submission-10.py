class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1 = sorted(s1)
        for r in range(len(s2)):
            if r - l + 1 == len(s1):
                substr = s2[l: r + 1]
                substr = sorted(substr)
                if substr == s1:
                    return True
                l += 1
        return False