class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1:
            return 1
        if x == -1:
            return 1.0 if n % 2 == 0 else -1.0
        if x == 0 or n < -100000:
            return 0.0
        curr = x
        for i in range(abs(n) - 1):
            x *= curr
        return x if n > 0 else 1 / x










































