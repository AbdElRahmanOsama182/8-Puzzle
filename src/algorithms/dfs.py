from algorithms.search_algorithm import SearchAlgorithm
from collections import deque

class DFS(SearchAlgorithm):
    def __init__(self, goal_state):
        super().__init__(goal_state)
    def search(self, initial_state,max_depth = 10000):
        state = int(initial_state)
        frontier = deque()
        explored = set()
        frontier.append((0, state))
        parent = {}
        parent[state] = -1
        # cost = {}
        # cost[state] = 0
        self.number_of_nodes_expanded = 0
        self.search_depth = 0
        self.path_to_goal = []
        self.states_to_goal = []

        while frontier:
            depth, state = frontier.pop()
            state_str = str(state)
            if self.is_goal(state_str):
                self.rebuild_path(parent)
                # self.search_depth = cost[state]
                self.search_depth = depth
                return True
            if state in explored:
                continue
            explored.add(state)
            self.number_of_nodes_expanded += 1
            for child, dir in self.state_handler.get_children(state_str):
                if child not in explored and child not in parent:#parent list as the frontier
                    # new_cost = cost[state] + 1
                    # if child not in cost or new_cost < cost[child]:
                    #     cost[child] = new_cost
                    if depth < max_depth:
                        frontier.append((depth+1, child))
                        parent[child] = (state, dir)          
        return False
