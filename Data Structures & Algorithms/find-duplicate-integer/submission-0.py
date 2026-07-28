class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = {}
        greatest = 0
        for num in nums:
            if num in duplicate:
                duplicate[num] += 1
                return num
            else:
                duplicate[num] = 1
        
        