class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        secLast,Last = 1,1
        for i in range(n - 1):
            temp = secLast 
            secLast = secLast + Last
            Last = temp
        return secLast
