class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums2)):
            if nums1[m] == 0:
                nums1[m] = nums2[i]
                m+=1
            else:
                continue
        return nums1.sort()