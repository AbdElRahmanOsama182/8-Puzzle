from algorithms.search_algorithm import SearchAlgorithm
from collections import deque

class IterativeDFS(SearchAlgorithm):
    def __init__(self, goal_state):
        super().__init__(goal_state)

    def search(self, initial_state):
        cur_iteration_depth = 0
        
        self.search_depth = 0
        self.path_to_goal = []
        self.states_to_goal = []
        self.number_of_nodes_expanded = 0
        frontier = deque()
        parent = {}
       

        while True:
            state = int(initial_state)
            frontier.append((0, state))
            cost = {}
            parent[state] = -1
            cost[state] = 0

            while frontier:
                depth, state = frontier.pop()
                state_str = str(state)


                if self.is_goal(state_str):
                    self.rebuild_path(parent)
                    self.search_depth = depth
                    print(cur_iteration_depth )
                    return True
                
                if depth >= cur_iteration_depth: 
                    continue

                self.number_of_nodes_expanded += 1
                for child, dir in self.state_handler.get_children(state_str):
                    if child not in cost or cost[child] > depth + 1:
                        frontier.append((depth+1, child))
                        parent[child] = (state, dir)  
                        cost[child] = depth + 1
            cur_iteration_depth += 1
       
        return False  
