class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = {}
        for i in range(len(s)):
            if s[i] not in char:
                char[s[i]] = 1
            else:
                char[s[i]] +=1
        for i in range(len(s)):
            if char[s[i]] == 1:
                return i
        return -1