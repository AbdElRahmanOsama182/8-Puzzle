from search_algorithm import SearchAlgorithm
from state_handler import StateHandler

class AStar(SearchAlgorithm):
    def __init__(self, heuristics):
        self.GOAL_STATE="012345678"
        self.heuristics=heuristics
        self.state_handler = StateHandler()
    