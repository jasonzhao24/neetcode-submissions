class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        visited = set()

        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l+=1
            visited.add(s[r])
            longest = max(longest,r-l+1)
        return longest