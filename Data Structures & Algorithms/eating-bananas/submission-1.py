class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high = 1, max(piles)
        res = 0
        
        while low <= high:
            currHours = 0
            mid = (low + high) // 2
            for i in range(len(piles)):
                currHours += math.ceil(piles[i] / mid)
            if currHours <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res
            

