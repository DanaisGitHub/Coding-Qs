Given a graph represented as an adjacency list and a starting vertex, 
implement a function dfsTraversal to perform a depth-first traversal of the graph starting from the specified vertex. 
The function should return a list of vertices visited during the traversal.

function dfsTraversal(graph: dict, startVertex: int) -> List[int]:
    # Your implementation here


Example:
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}
startVertex = 1
print(dfsTraversal(graph, startVertex))  # Output: [1, 2, 4, 5, 6, 3]

Please analyze the time complexity (Big O) of your solution.

Time Complexity (Big O): The time complexity of the solution should be O(V + E), where V is the number of vertices and E is the number of edges in the graph.
