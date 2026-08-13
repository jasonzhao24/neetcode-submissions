class Solution:
    def maxScore(self, s: str) -> int:
        best = 0
        for i in range(1, len(s)):  
            left = s[:i] ## count from 0 to i
            right = s[i:] # count from i to len(s)
            score = left.count('0') + right.count('1')
            best = max(best, score)
        return best
                
                
