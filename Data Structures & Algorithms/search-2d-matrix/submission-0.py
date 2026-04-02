class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)
        row_index = -1
        while l < r:
            mid = (l+r)//2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row_index = mid
                break
            elif matrix[mid][0] > target:
                r = mid
            else:
                l = mid+1
        if row_index == -1:
            return False
        row = matrix[row_index]
        l, r = 0, len(row)
        while l < r:
            mid = (l+r)//2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                r = mid
            else:
                l = mid+1
        return False