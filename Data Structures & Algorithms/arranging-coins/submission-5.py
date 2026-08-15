class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 1:
            return 0
        comp = 0
        curr = 0
        for i in range(1,n+1):
            curr += i
            if curr > n:
                return comp
            else:
                comp +=1
            
        return comp