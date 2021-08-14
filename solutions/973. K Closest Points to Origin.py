import heapq
import numpy as np
​
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        # Initialize max heap
        # push first k in heap
        for idx in range(k):
            distance = self.getDistance(points[idx])
            maxHeap.append((-distance, idx))
        heapq.heapify(maxHeap)
        # loop over remaining and pushpop while mainting heap size of k
        for idx in range(k, len(points)):
            distance = self.getDistance(points[idx])
            heapq.heappushpop(maxHeap, (-distance, idx))
        return [points[pair[1]] for pair in maxHeap]
        
    def getDistance(self, point):
        return (point[0] ** 2 + point[1] ** 2) ** 0.5
