class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                r, c = row, col
                if grid[r][c] == 0:
                    continue
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                currentSize = 0
                queue = [(r, c)]
                while queue:
                    r, c = queue.pop(0)
                    currentSize += 1
                    for r0, c0 in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if (0 <= r0 < len(grid) and 0 <= c0 < len(grid[0])) and grid[r0][c0] == 1 and (r0, c0) not in visited:
                            visited.add((r0, c0))
                            queue.append((r0, c0))
                maxArea = max(maxArea, currentSize)
        return maxArea 
