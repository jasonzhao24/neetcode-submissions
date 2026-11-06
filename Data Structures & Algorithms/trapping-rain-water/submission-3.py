class Solution:
    def trap(self, height: List[int]) -> int:
        sum = 0
        l = 0
        r = len(height) - 1
        max_left = height[l]
        max_right = height[r]
        while l < r:
            if max_left < max_right:
                l+=1
                if height[l] > max_left:
                    max_left = height[l]
                else:
                    sum += max_left - height[l]
            else:
                r-=1
                if height[r] > max_right:
                    max_right = height[r]
                else:
                    sum+= max_right-height[r]
        return sum           
            