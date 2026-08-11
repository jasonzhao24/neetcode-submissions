class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxFreq = 0
        ans = 0
        map = {}
        for r in range(len(s)):
            if s[r] not in map or s[r] in map: ## if curr char not in map, add it iin
                if s[r] in map:   
                    map[s[r]] += 1
                else:
                    map[s[r]] = 1
                if map[s[r]] > maxFreq: ## Check if the freq of the char currently is greater than the maxFreq variable
                    maxFreq = map[s[r]]
                if (r-l+1) - maxFreq >k: ## If the window size - maxFreq is greater than k, then the window is invalid and we increment l
                    map[s[l]] -=1
                    l+=1
                ans = max (ans,r - l + 1) 
           
        return ans
                