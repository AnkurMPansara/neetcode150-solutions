class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        r, c = len(matrix), len(matrix[0])

        def spiral(top, bottom, left, right):
            if top > bottom or left > right:
                return
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
            spiral(top, bottom, left, right)
        
        spiral(0, r-1, 0, c-1)
        return res