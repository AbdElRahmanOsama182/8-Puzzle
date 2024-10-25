from heuristics.heuristic import Heuristic

class ManhattanDistance(Heuristic):
    def __init__(self, board_dim:int = 3):
        super().__init__(board_dim)

    def manhattan_distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def heuristic(self, state, goal_state):
        sum = 0
        for i in range(len(state)):
            x1, y1 = i // self.board_dim, i % self.board_dim
            x2, y2 = goal_state.index(state[i]) // self.board_dim, goal_state.index(state[i]) % self.board_dim
            sum += self.manhattan_distance(x1, y1, x2, y2)
        return sum
