class Solution:
    # Time = O(mn)
    # Space = O(mn)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        self.helperSpiral(matrix, spiral, 0, len(matrix)-1, 0, len(matrix[0])-1)
        return spiral
    
    def helperSpiral(self, matrix, spiral, firstRow, lastRow, firstCol, lastCol):
        if firstRow > lastRow or firstCol > lastCol:
            return 
        # Traverse the outside
        for idx in range(firstCol, lastCol+1):
            spiral.append(matrix[firstRow][idx])
        for idx in range(firstRow+1, lastRow+1):
            spiral.append(matrix[idx][lastCol])
        for idx in reversed(range(firstCol, lastCol)):
            if firstRow == lastRow:
                break
            spiral.append(matrix[lastRow][idx])
        for idx in reversed(range(firstRow+1, lastRow)):
            if firstCol == lastCol:
                break
            spiral.append(matrix[idx][firstCol])
        self.helperSpiral(matrix, spiral, firstRow+1, lastRow-1, firstCol+1, lastCol-1)
        return
        
