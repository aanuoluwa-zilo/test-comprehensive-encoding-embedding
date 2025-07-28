# Complex Algorithm Implementation 3
import heapq
from typing import List, Tuple, Optional

class GraphProcessor3:
    def __init__(self):
        self.graph = {}
        self.visited = set()
    
    def add_edge(self, from_node: str, to_node: str, weight: int):
        if from_node not in self.graph:
            self.graph[from_node] = []
        self.graph[from_node].append((to_node, weight))
    
    def dijkstra_shortest_path(self, start: str, end: str) -> Optional[List[str]]:
        if start not in self.graph or end not in self.graph:
            return None
        
        distances = {node: float('infinity') for node in self.graph}
        distances[start] = 0
        previous = {}
        pq = [(0, start)]
        
        while pq:
            current_distance, current_node = heapq.heappop(pq)
            
            if current_node == end:
                break
            
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in self.graph.get(current_node, []):
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
        
        # Reconstruct path
        path = []
        current = end
        while current in previous:
            path.append(current)
            current = previous[current]
        path.append(start)
        path.reverse()
        
        return path if distances[end] != float('infinity') else None

# Usage
processor = GraphProcessor3()
processor.add_edge('A', 'B', 4)
processor.add_edge('A', 'C', 2)
processor.add_edge('B', 'D', 3)
processor.add_edge('C', 'D', 1)
path = processor.dijkstra_shortest_path('A', 'D')
print(f"Shortest path: {path}")
