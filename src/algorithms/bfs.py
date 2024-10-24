from search_algorithm import SearchAlgorithm
from collections import deque

class BFS(SearchAlgorithm):
    def __init__(self):
        super().__init__()
    
    def search(self, state):
        frontier=deque()
        frontier.append(state) # initial state
        visited = {}
        visited[state]=True

        while frontier:
            state=frontier.popleft()
            state_str = self.state_handler.convert_state_to_string(state)
            if self.is_goal(state_str):
                return True
            
            if not self.is_solvable(state_str):
                return False
            
            # check children
            for child in self.state_handler.get_children():
              if not visited[child]:
                  frontier.append(child)
                  visited[child] = True

        return False
            