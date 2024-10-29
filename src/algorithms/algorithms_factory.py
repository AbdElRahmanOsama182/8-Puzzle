from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.iterative_dfs import IterativeDFS
from algorithms.a_star import AStar
from heuristics.heuristic import Heuristic
from algorithms.greedy_bfs import GreedyBFS 

class AlgorithmsFactory:
    # Factory class for creating search algorithms
    def get_algorithm(self, algorithm_name, heuristic:Heuristic = None
                        , goal_state="123456789"):
        if algorithm_name == "bfs":
            return BFS(goal_state)
        elif algorithm_name == "dfs":
            return DFS(goal_state)
        elif algorithm_name == "iddfs":
            return IterativeDFS(goal_state)
        elif algorithm_name == "a*":
            return AStar(goal_state=goal_state,heuristic=heuristic)
        elif algorithm_name == "gbfs":
            return GreedyBFS(goal_state=goal_state,heuristic=heuristic)
        else:
            # let default be BFS
            return BFS(goal_state)
            

