class Solution:
    def isHappy(self, n: int) -> bool:
        tracked = {}
        total = 0
        currNum = n
        while total != 1:
            total = 0
            for digit in str(currNum):
                total += int(digit) ** 2 
            if total in tracked:
                return False
            tracked[total] = 1
            currNum = total
 
        return True