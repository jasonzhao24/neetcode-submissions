class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined = ""
        l,r = 0, 0
        while l < len(word1) or r < len(word2):
            if l < len(word1):
                combined += word1[l]
            if r < len(word2):
                combined+= word2[r]
            l+=1
            r+=1
        return combined