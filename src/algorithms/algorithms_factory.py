from dfs import DFS
from bfs import BFS
from iterative_dfs import IterativeDFS
from a_star import AStar
from heuristics.heuristic import Heuristic

class AlgorithmsFactory:
    def get_algorithm(self, algorithm_name, heuristics:Heuristic = None):
        if algorithm_name == "bfs":
            return BFS()
        elif algorithm_name == "dfs":
            return DFS()
        elif algorithm_name == "iterative_dfs":
            return IterativeDFS()
        elif algorithm_name == "a_star":
            return AStar(heuristics=heuristics)
        else:
            # let default be BFS
            return BFS()
            

