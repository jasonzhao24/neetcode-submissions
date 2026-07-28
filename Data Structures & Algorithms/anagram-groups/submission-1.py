class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for element in strs:
            key = "".join(sorted(element))
            if key in anagram:
                anagram[key].append(element)
            else:
                anagram[key] = [element]
        return list(anagram.values())