class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        half = math.floor(len(nums)/2)
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 1
            else:
                map[nums[i]] +=1
        for key,value in map.items():
            if value >= half:
                return key
            