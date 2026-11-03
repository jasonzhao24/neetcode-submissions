class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row, cols = len(matrix), len(matrix[0])
        low,high = 0, (row*cols) - 1
        while low <= high:
            mid = (low+high) // 2
            r = mid // cols
            c = mid % cols
            if matrix[r][c] < target:
                low = mid+1
            elif matrix[r][c] > target:
                high = mid-1
            else:
                return True
        return False