from euclidean_distance import EuclideanDistance
from manhattan_distance import ManhattanDistance

class HeuristicsFactory:
    def get_heuristics(self, heuristic_name):
        if heuristic_name == "euclidean":
            return EuclideanDistance()
        elif heuristic_name == "manhattan":
            return ManhattanDistance()
        else:
            # let default heuristics be manhattan distance
            return ManhattanDistance()
            

