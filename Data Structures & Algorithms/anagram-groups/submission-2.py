class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_counter = {}

        for str in strs:
            counter = {}
            for c in str:
                counter[c] = 1 + counter.get(c, 0)
            key = tuple(sorted(counter.items()))

            if key in my_counter:
                my_counter[key].append(str)
            else:
                my_counter[key] = [str]
        res = []
        for value in my_counter.values():
            res.append(value)
        return (res)