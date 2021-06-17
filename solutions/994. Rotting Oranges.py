# Time = O(V + E) | Sapce = O(V)
# Idea: Get a count of healthy oranges and append all infected oranges in queue. 
# Run a bfs search using a while loop as long as queue isn't empty and healthy count is > 0.
# Increase the minute timer. Perform a for loop on the current number of infected oranges in queue,
# pop the front, and search for neighboring healthy oranges and infect - make sure to decrease the count of healthy oranges
# when found, modify inplace grid when infect, and append in queue the infected oranges.
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find # of healthy oranges
        # append all infected oranges in queue
        if len(grid) == 0:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        healthy_count = 0
        queue = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    healthy_count += 1
                elif grid[row][col] == 2:
                    queue.append([row, col])
        minutes_elapsed = 0
        while len(queue) > 0 and healthy_count > 0:
            minutes_elapsed += 1
            for _ in range(len(queue)):
                row, col = queue.pop(0)
                neighbors = self.getNeighbors(grid, row, col)
                for neighbor in neighbors:
                    row, col = neighbor
                    if grid[row][col] == 0 or grid[row][col] == 2:
                        continue
                    healthy_count -= 1
                    grid[row][col] = 2
                    queue.append([row, col])
        return minutes_elapsed if healthy_count == 0 else -1
    
    def getNeighbors(self, grid, i, j):
        neighbors = []
        if i > 0:
            neighbors.append([i-1, j])
        if j > 0:
            neighbors.append([i, j-1])
        if i+1 < len(grid):
            neighbors.append([i+1, j])
        if j+1 < len(grid[0]):
            neighbors.append([i, j+1])
        return neighbors
