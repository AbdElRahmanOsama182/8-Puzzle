from algorithms.search_algorithm import SearchAlgorithm
from algorithms.algorithms_factory import AlgorithmsFactory
from heuristics.heuristics_factory import HeuristicsFactory
from state_handler import StateHandler
class PuzzleBoard:
    def __init__(self, state:int, algorithm_name:str, heuristic_name:str=None):
        self.state=state
        heuristic = None
        algorithm_factory=AlgorithmsFactory()
        if heuristic_name is not None:
            heuristic_factory = HeuristicsFactory()
            heuristic=heuristic_factory.get_heuristics(heuristic_name)
        self.algorithm = algorithm_factory.get_algorithm(algorithm_name, heuristic)
        self.state_handler = StateHandler()

    def solve(self):
        state_str=self.state_handler.convert_state_to_string(self.state)
        if self.state_handler.is_solvable(state_str):
            success = self.algorithm.search(self.state)
        else:
            success = False
        # We would want to get number of nodes expanded & path to goal
        # & search depth & path to goal cost from algorithm class
        # and we should get the runtime duration for this function
