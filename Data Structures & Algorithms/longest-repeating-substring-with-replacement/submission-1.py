class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxFreq = 0
        ans = 0
        map = {}
        for r in range(len(s)):
            if s[r] not in map:
                map[s[r]] = 1
                if map[s[r]] > maxFreq:
                    maxFreq = map[s[r]]
                if (r-l+1) - maxFreq >k:
                    map[s[l]] -=1
                    l+=1
                ans = max (ans,r - l + 1)
            else:
                map[s[r]] +=1
                if map[s[r]] > maxFreq:
                    maxFreq = map[s[r]]
                if (r-l+1) - maxFreq >k:
                    map[s[l]] -=1
                    l+=1
                ans = max (ans,r - l + 1)               
        return ans
                