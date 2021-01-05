class Solution:
    # Idea: Seach each row. If it's not in a row by checking first and last element, keep going.
    # If the first element is larger than the target, return False as the rest won't have the target.
    # If the target is in the row, use binary search. 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found = False
        for idx in range(len(matrix)):
            if matrix[idx][0] > target:
                return False
            if self.helperSearch(matrix, target, idx):
                return True
        return found    
    
    def helperSearch(self, matrix, target, row):
        if not (matrix[row][0] <= target <= matrix[row][len(matrix[0])-1]):
            return False
        else:
            return self.binarySearch(matrix, target, row)  # check if target is in the vector
    
    def binarySearch(self, matrix, target, row):
        left, right = 0, len(matrix[0]) - 1
        found = False
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return found
