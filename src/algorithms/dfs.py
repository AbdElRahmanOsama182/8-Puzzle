from algorithms.search_algorithm import SearchAlgorithm
from collections import deque
import time

class DFS(SearchAlgorithm):
    def __init__(self, goal_state):
        super().__init__(goal_state)
    def search(self, initial_state):
        state = int(initial_state)
        frontier = deque()
        explored = set()
        frontier.append((0, state))
        parent = {}
        parent[state] = -1

        self.number_of_nodes_expanded = 0
        self.search_depth = 0
        self.path_to_goal = []
        self.states_to_goal = []

        start_time=time.time()
        while frontier:
            depth, state = frontier.pop()
            explored.add(state)
            self.number_of_nodes_expanded += 1
            self.search_depth = max(self.search_depth, depth) 
            
            state_str = str(state)
            if self.is_goal(state_str):
                self.running_time=time.time()-start_time
                self.rebuild_path(parent)
                return True

            for child in reversed(self.state_handler.get_children(state_str)):
                if child not in explored and child not in parent: # parent map chechking if the child is already in the frontier
                    frontier.append((depth+1, child))
                    parent[child] = state 
                       
        self.running_time=time.time()-start_time   
        return False
