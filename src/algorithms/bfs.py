from algorithms.search_algorithm import SearchAlgorithm
from collections import deque
import time

class BFS(SearchAlgorithm):
    def __init__(self, goal_state:str="123456789"):
        super().__init__(goal_state)
    
    def search(self, state):
        # initialize the frontier with the initial state
        state=int(state)
        frontier=deque()
        frontier.append(state)
        visited = {}
        visited[state]=True
        parent = {}
        parent[state] = -1
        self.search_depth = 0
        self.number_of_nodes_expanded = 0
        self.path_to_goal = []
        self.states_to_goal = []
        start_time=time.time()

        # while frontier is not empty
        while frontier:
            level_size = len(frontier)
            # for each node in the current level
            for i in range(level_size):
                state:int=frontier.popleft()
                state_str = str(state)
                # increment the number of nodes expanded
                self.number_of_nodes_expanded += 1
                # check if the state is the goal state 
                if self.is_goal(state_str):
                    self.running_time=time.time()-start_time   
                    self.rebuild_path(parent)
                    return True
                # get the children of the state
                for child in self.state_handler.get_children(state_str):
                    if not visited.get(child, False):
                        frontier.append(child)
                        parent[child] = state
                        visited[child] = True
            self.search_depth += 1
        self.search_depth -= 1 # root is at zero depth
        self.running_time=time.time()-start_time   
        return False
            