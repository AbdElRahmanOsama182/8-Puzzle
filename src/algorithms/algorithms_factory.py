from algorithms.dfs import DFS
from algorithms.bfs import BFS
from algorithms.iterative_dfs import IterativeDFS
from algorithms.a_star import AStar
from heuristics.heuristic import Heuristic

class AlgorithmsFactory:
    def get_algorithm(self, algorithm_name, heuristics:Heuristic = None
                      , goal_state="012345678"):
        if algorithm_name == "bfs":
            return BFS(goal_state)
        elif algorithm_name == "dfs":
            return DFS(goal_state)
        elif algorithm_name == "iterative_dfs":
            return IterativeDFS(goal_state)
        elif algorithm_name == "a_star":
            return AStar(goal_state=goal_state,heuristics=heuristics)
        else:
            # let default be BFS
            return BFS(goal_state)
            

