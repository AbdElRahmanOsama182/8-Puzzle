from algorithms.search_algorithm import SearchAlgorithm
from heuristics.heuristic import Heuristic
from puzzle.state_handler import StateHandler
import heapq
import time

class GreedyBFS(SearchAlgorithm):

    def __init__(self, goal_state, heuristic:Heuristic):
        self.heuristic = heuristic
        super().__init__(goal_state)

    def search(self, state:str):
        # initialize the frontier with the initial state
        state = int(state)
        frontier = []
        explored = set()
        heapq.heappush(frontier, (0, state))
        parent = {}
        parent[state] = -1
        self.number_of_nodes_expanded = 0
        self.search_depth = 0
        self.path_to_goal = []
        self.states_to_goal = []
        start_time = time.time()

        # while frontier is not empty
        while frontier:
            # get the state with the lowest cost
            _, state = heapq.heappop(frontier)
            state_str = str(state)
            # check if the state has been explored
            if state in explored:
                continue
            # increment the number of nodes expanded
            self.number_of_nodes_expanded += 1
            # check if the state is the goal state
            if self.is_goal(state_str):
                self.running_time=time.time()-start_time  
                self.rebuild_path(parent)
                self.search_depth = len(self.path_to_goal)
                return True
            # add the state to the explored
            explored.add(state)
            # get the children of the state
            for child in self.state_handler.get_children(state_str):
                if child not in explored:
                    priority = self.heuristic.heuristic(str(child), self.goal_state)
                    heapq.heappush(frontier, (priority, child))
                    parent[child] = state
        self.running_time=time.time()-start_time   
        return False