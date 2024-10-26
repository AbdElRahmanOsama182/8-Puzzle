from algorithms.search_algorithm import SearchAlgorithm
from heuristics.heuristic import Heuristic
from puzzle.state_handler import StateHandler
import queue

class AStar(SearchAlgorithm):
    def __init__(self, goal_state, heuristic:Heuristic):
        self.heuristic = heuristic
        super().__init__(goal_state)
    def search(self, state:str):
        # print(state)
        state = int(state)
        frontier = queue.PriorityQueue()
        explored = set()
        frontier.put((0, state))
        parent = {}
        parent[state] = -1
        cost = {}
        cost[state] = 0
        self.number_of_nodes_expanded = 0
        self.search_depth = 0
        self.path_to_goal = []
        self.states_to_goal = []

        while not frontier.empty():
            _, state = frontier.get()
            state_str = str(state)
            if self.is_goal(state_str):
                self.rebuild_path(parent)
                self.search_depth = cost[state]
                return True
            if state in explored:
                continue
            explored.add(state)
            self.number_of_nodes_expanded += 1
            for child in self.state_handler.get_children(state_str):
                if child not in explored:
                    new_cost = cost[state] + 1
                    if child not in cost or new_cost < cost[child]:
                        cost[child] = new_cost
                        priority = new_cost + self.heuristic.heuristic(str(child), self.goal_state)
                        frontier.put((priority, child))
                        parent[child] = state
        return False