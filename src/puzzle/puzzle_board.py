from algorithms.search_algorithm import SearchAlgorithm
from algorithms.algorithms_factory import AlgorithmsFactory
from heuristics.heuristics_factory import HeuristicsFactory
from puzzle.state_handler import StateHandler
from puzzle.search_result import SearchResult

class PuzzleBoard:

    def __init__(self, state:str, algorithm_name:str, heuristic_name:str=None
                    , goal_state:str="012345678"):
        self.state=state
        self.goal_state=goal_state
        heuristic = None
        algorithm_factory=AlgorithmsFactory()
        if heuristic_name is not None:
            heuristic_factory = HeuristicsFactory()
            heuristic=heuristic_factory.get_heuristics(heuristic_name)
        self.state_handler = StateHandler(self.goal_state)
        self.state = self.state_handler.increment_state(state)
        self.goal_state = self.state_handler.increment_state(self.goal_state)
        self.state_handler.set_goal_state(self.goal_state) # after incrementing
        self.algorithm = algorithm_factory.get_algorithm(algorithm_name, heuristic, self.goal_state)

    def solve(self):
        # check if the state is solvable before searching
        if self.state_handler.is_solvable(self.state):
            success = self.algorithm.search(self.state)
        else:
            success = False
        # print("Path to goal: " + ''.join(self.algorithm.get_path_to_goal()))
        # We would want to get number of nodes expanded & path and states to goal &
        # & search depth & path to goal cost from algorithm class
        # and we should get the runtime duration for this function
        return SearchResult(success, self.algorithm.get_running_time(), 
                            self.algorithm.get_number_of_nodes_expanded(),
                            self.algorithm.get_search_depth(),
                            self.algorithm.get_path_to_goal(),
                            self.algorithm.get_cost_to_goal(),
                            self.algorithm.get_states_to_goal())
