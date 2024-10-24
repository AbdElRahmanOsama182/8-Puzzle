from search_algorithm import SearchAlgorithm

class AStar(SearchAlgorithm):
    def __init__(self, heuristics):
        self.GOAL_STATE="012345678"
        self.heuristics=heuristics
    