from algorithms.search_algorithm import SearchAlgorithm
from collections import deque

class IterativeDFS(SearchAlgorithm):
    def __init__(self, goal_state):
        super().__init__(goal_state)

    def search(self, initial_state):
        cur_iteration_depth = 0
        # frontier_max_size = 0
        self.search_depth = 0
        self.path_to_goal = []
        self.states_to_goal = []
        self.number_of_nodes_expanded = 0
        frontier = deque()
        parent = {}
       

        while True:
            state = int(initial_state)
            frontier.append((0, state))
            depths = {}
            parent[state] = -1
            depths[state] = 0

            while frontier:
                # frontier_max_size = max(frontier_max_size, len(frontier))
                cur_depth, state = frontier.pop()
                self.number_of_nodes_expanded += 1

                state_str = str(state)

                if self.is_goal(state_str):
                    self.rebuild_path(parent)
                    self.search_depth = cur_depth
                    # print("frontier_max_size:", frontier_max_size)
                    # print("number_of_nodes_expanded"+self.number_of_nodes_expanded)
                    return True
                
                # if depth >= cur_iteration_depth: 
                #     continue

                for child, dir in reversed(self.state_handler.get_children(state_str)):
                    if (child not in depths or depths[child] > cur_depth + 1) and cur_depth < cur_iteration_depth:
                        frontier.append((cur_depth+1, child))
                        parent[child] = (state, dir)  
                        depths[child] = cur_depth + 1
                        
            cur_iteration_depth += 1
       
        return False  
