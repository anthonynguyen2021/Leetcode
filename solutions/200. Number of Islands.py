class Solution:
    # Time Complexity: O(V + E)
    # Space Complexity: O(V)
    def numIslands(self, grid: List[List[str]]) -> int:
        size = 0
        visited = [[False for entry in row] for row in grid]
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                size = self.islandDFS(grid, i, j, visited, size)
        return size
    
    def islandDFS(self, grid, i, j, visited, size):
        current = 0
        stack = [[i, j]]
        while stack:
            [i, j] = stack.pop()
            if visited[i][j]:
                continue
            visited[i][j] = True
            if grid[i][j] == '0':
                continue
            current += 1
            getNeighbors = self.helperNeighbors(i, j, visited)
            for node in getNeighbors:
                stack.append(node)
        if current > 0:
            size = size + 1
        return size
        
    def helperNeighbors(self, i, j, visited):
        neighbors = []
        if i > 0 and not visited[i-1][j]:
            neighbors.append([i-1, j])
        if i < len(visited) - 1 and not visited[i+1][j]:
            neighbors.append([i+1, j])
        if j > 0 and not visited[i][j-1]:
            neighbors.append([i, j-1])
        if j < len(visited[0]) - 1 and not visited[i][j+1]:
            neighbors.append([i, j+1])
