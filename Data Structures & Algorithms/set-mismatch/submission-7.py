class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        map = {}
        result = []
        curr = 1
        for i in range(len(nums)):
            
            if nums[i] not in map:
                map[nums[i]] = 1
            else:
                result.append(nums[i])
        for curr in range(1, len(nums) + 1):
            if curr not in map:
                result.append(curr)
                break

        return result