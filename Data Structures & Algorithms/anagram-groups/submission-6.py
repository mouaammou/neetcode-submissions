class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_counter = {}

        for str in strs:
            counter = [0] * 26
            for c in str:
                counter[ord(c) - ord('a')] += 1

            key = tuple(counter)

            if key in my_counter:
                my_counter[key].append(str)
            else:
                my_counter[key] = [str]

        return list(my_counter.values())