from algorithms.search_algorithm import SearchAlgorithm
from collections import deque
import time

class IterativeDFS(SearchAlgorithm):

    def __init__(self, goal_state):
        super().__init__(goal_state)

    def search(self, initial_state):
        # initialize the frontier with the initial state
        cur_iteration_depth = 0
        self.search_depth = 0
        self.path_to_goal = []
        self.states_to_goal = []
        self.number_of_nodes_expanded = 0
        frontier = deque()
        start_time=time.time()

        is_solvable = self.state_handler.is_solvable(initial_state)
        # while is_solvable try to find the goal state with increasing depth
        while is_solvable:
            
            # initialize the frontier with the initial state
            state = int(initial_state)
            frontier.append(state)
            depths = {}
            depths[state] = 0
            parent = {}
            parent[state] = -1
            # while frontier is not empty
            while frontier:
                state = frontier.pop()
                cur_depth = depths[state]

                self.number_of_nodes_expanded += 1

                state_str = str(state)
                # check if the state is the goal state
                if self.is_goal(state_str):
                    self.running_time=time.time()-start_time
                    self.rebuild_path(parent)
                    self.search_depth = cur_iteration_depth
                    return True
                # get the children of the state
                for child in reversed(self.state_handler.get_children(state_str)):
                    if (child not in depths or depths[child] > cur_depth + 1) and cur_depth < cur_iteration_depth:
                    # if (child not in depths) and cur_depth < cur_iteration_depth:
                        # frontier.append((cur_depth+1, child))
                        frontier.append(child)
                        # parent[child] = (state, dir)  
                        parent[child] =  state
                        depths[child] = cur_depth + 1
                        
            cur_iteration_depth += 1
        self.running_time=time.time()-start_time
        return False  
