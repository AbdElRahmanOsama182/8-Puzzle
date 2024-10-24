from algorithms.search_algorithm import SearchAlgorithm
from collections import deque

class BFS(SearchAlgorithm):
    def __init__(self):
        super().__init__()
    
    def search(self, state):
        frontier=deque()
        frontier.append(state) # initial state
        visited = {}
        visited[state]=True
        parent = {}
        parent[state] = -1

        self.search_depth = 0
        self.number_of_nodes_expanded = 0
        while frontier:
            level_size = len(frontier)
            for i in range(level_size):
                state=frontier.popleft()
                state_str = self.state_handler.convert_state_to_string(state)
                
                self.number_of_nodes_expanded += 1
                
                if self.is_goal(state_str):
                    self.rebuild_path(parent)
                    return True
                for child, dir in self.state_handler.get_children(state_str):
                    if not visited.get(child, False):
                        frontier.append(child)
                        parent[child] = (state, dir)
                        visited[child] = True
            self.search_depth += 1
        self.search_depth -= 1 # root is at zero depth
        return False
            