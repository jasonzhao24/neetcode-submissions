class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        list = {}
        for i in nums:
            if i in list:
                list[i] += 1
            else:
                list[i] = 1
        for key, value in list.items():
            if value == 1:
                return key