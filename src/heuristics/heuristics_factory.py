from heuristics.euclidean_distance import EuclideanDistance
from heuristics.manhattan_distance import ManhattanDistance
from heuristics.linear_conflict import LinearConflict

class HeuristicsFactory:
    # Factory class for creating heuristics
    def get_heuristics(self, heuristic_name):
        if heuristic_name == "euclidean":
            return EuclideanDistance()
        elif heuristic_name == "manhattan":
            return ManhattanDistance()
        elif heuristic_name == "linear_conflict":
            return LinearConflict()
        else:
            # let default heuristics be manhattan distance
            return ManhattanDistance()
            

