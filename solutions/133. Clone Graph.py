"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
​
class Solution:
    # Time: O(V + E)
    # Space: O(V + E) - Considering the edge sets
    # Explanation: Create a dictionary which denotes if we visited a node or not. We perform a 
    # DFS search via recursion and clone the node and copy its neighbors using a list comprehension and 
    # using a recursion method.
    def cloneGraph(self, node: 'Node') -> 'Node':
        dictionaryClone = {}
        self.cloneDFS(node, dictionaryClone)
        return dictionaryClone[node]
    
    def cloneDFS(self, node, dictionaryClone):
        if not node:
            dictionaryClone[node] = node
        elif node not in dictionaryClone:
            dictionaryClone[node] = Node(node.val)
            dictionaryClone[node].neighbors = [self.cloneDFS(point, dictionaryClone) for point in node.neighbors]
        return dictionaryClone[node]
        
