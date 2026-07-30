class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longestSub = 0
        
        for num in num_set:
            if num-1 in num_set:
                continue 
            else:
                curr_num = num
                currLen = 0
                while curr_num in num_set:
                    curr_num += 1
                    currLen +=1
                    if currLen > longestSub:
                        longestSub = currLen
                    else:
                        continue
        return longestSub
