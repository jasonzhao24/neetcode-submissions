class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if count not in nums:
                return count
            count +=1
        return len(nums)