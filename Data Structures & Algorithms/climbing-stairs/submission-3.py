class Solution:
    def climbStairs(self, n: int) -> int:
        secLast,Last = 1,1 ## representing n-1 and n

        for i in range(n - 1):
            temp = secLast ## saving the second last so then we can add it onto the next
            secLast += Last
            Last = temp
        return secLast
