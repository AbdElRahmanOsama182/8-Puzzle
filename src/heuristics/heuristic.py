from abc import ABC, abstractmethod

class Heuristic:
    def __init__(self, board_dim:int = 3):
        self.board_dim = board_dim
    
    @abstractmethod
    def heuristic(self, state:str, goal_state):
        pass