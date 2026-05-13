class Solution:
    def encode(self, strs: List[str]) -> str:
            res = ""

            for s in strs:
                sep = f"*{len(s)}*"
                res += sep + s
            return res
    

    def decode(self, s: str) -> List[str]:
            
            i = 0
            res = []
            while i < len(s):
                if s[i] == '*':
                    j = i + 1
                    while j < len(s) and s[j] != '*':
                        j += 1
                    # print(s[i+1:j])
                    len_s = int(s[i+1:j])
                    res.append(s[j+1: j+1+len_s])
                    i = len_s + j + 1
                else:
                    i+= 1
            return res
