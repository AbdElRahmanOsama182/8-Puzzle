from algorithms.search_algorithm import SearchAlgorithm
from puzzle.state_handler import StateHandler

class AStar(SearchAlgorithm):
    def __init__(self, heuristics):
        self.heuristics=heuristics
        super().__init__()